from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils.translation import gettext as _
from .forms import FeedbackForm
from .models import Feedback

@login_required
def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            messages.success(request, _('感谢您的反馈！'))
            return redirect('homepage:index')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/submit.html', {'form': form})

@login_required  # 只需要登录就可以查看
def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'feedback/list.html', {'feedbacks': feedbacks})

@user_passes_test(lambda u: u.is_staff)  # 只有管理员可以更改状态
def toggle_resolved(request, feedback_id):
    if request.method == 'POST':
        feedback = get_object_or_404(Feedback, id=feedback_id)
        feedback.is_resolved = not feedback.is_resolved
        feedback.save()
        messages.success(request, _('状态更新成功！'))
    return redirect('feedback:list')