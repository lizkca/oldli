from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class BlogPost(models.Model):
    LANGUAGE_CHOICES = [
        ('en', _('英语')),
        ('zh', _('中文')),
    ]

    title = models.CharField(_('标题'), max_length=200)
    content = models.TextField(_('内容'))
    language = models.CharField(_('语言'), max_length=2, choices=LANGUAGE_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('博客文章')
        verbose_name_plural = _('博客文章')
        ordering = ['-created_at']
