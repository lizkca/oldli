from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import SpeechRecord

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
