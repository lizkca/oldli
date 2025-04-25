from django.contrib import admin
from .models import Card, UserProgress

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['word', 'translation', 'language']
    list_filter = ['language']
    search_fields = ['word', 'translation']

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'card', 'is_mastered', 'review_count']
    list_filter = ['is_mastered', 'user']
