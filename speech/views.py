from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import SpeechRecord
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

@login_required
def speech_practice(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        audio_file = request.FILES.get('audio')
        if text:
            record = SpeechRecord.objects.create(
                user=request.user,
                text=text,
                user_recording=audio_file if audio_file else None
            )
    
    records = SpeechRecord.objects.filter(user=request.user)
    return render(request, 'speech/practice.html', {'records': records})

@login_required
@require_http_methods(["POST"])
def delete_record(request, record_id):
    try:
        # 获取记录并验证所有权
        record = SpeechRecord.objects.get(id=record_id, user=request.user)
        # 删除关联的音频文件
        if record.user_recording:
            record.user_recording.delete()
        # 删除记录
        record.delete()
        return JsonResponse({'status': 'success'})
    except SpeechRecord.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': '记录不存在或无权限删除'}, status=404)
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"删除记录失败: {str(e)}")
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
