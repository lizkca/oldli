from django import forms
from .models import Feedback
from django.utils.translation import gettext_lazy as _

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': _('请输入您的建议或反馈...')
            }),
        }