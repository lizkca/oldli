from django.db import models
from django.contrib.auth.models import User

class SpeechRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    text = models.TextField(verbose_name='英文文本')
    user_recording = models.FileField(upload_to='speech_records/', blank=True, null=True, verbose_name='用户录音')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '语音记录'
        verbose_name_plural = '语音记录'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.text[:30]}"
