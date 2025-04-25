from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    LANGUAGE_CHOICES = [
        ('zh', '中文'),
        ('en', '英文'),
    ]
    
    word = models.CharField(max_length=100, verbose_name='单词')
    translation = models.CharField(max_length=100, verbose_name='翻译')
    image = models.ImageField(upload_to='flashcards/', verbose_name='图片')
    pronunciation = models.FileField(upload_to='pronunciations/', blank=True, verbose_name='发音')
    example = models.TextField(verbose_name='例句', blank=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, verbose_name='语言')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = '单词卡'
        verbose_name_plural = '单词卡'
        
    def __str__(self):
        return f"{self.word} ({self.get_language_display()})"

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    is_mastered = models.BooleanField(default=False)
    review_count = models.IntegerField(default=0)
    last_reviewed = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = '学习进度'
        verbose_name_plural = '学习进度'
