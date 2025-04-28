from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('用户'))
    content = models.TextField(verbose_name=_('反馈内容'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('提交时间'))
    is_resolved = models.BooleanField(default=False, verbose_name=_('是否已处理'))

    class Meta:
        verbose_name = _('用户反馈')
        verbose_name_plural = _('用户反馈')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"