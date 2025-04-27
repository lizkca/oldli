from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FlashcardForm
from django.contrib import messages
from django.utils.translation import gettext as _
from .models import Card, UserProgress
import random

@login_required
def study(request):
    # 获取用户选择的学习语言
    study_language = request.GET.get('lang', 'en')
    
    # 获取用户还未掌握的卡片
    learned_cards = UserProgress.objects.filter(
        user=request.user,
        is_mastered=True
    ).values_list('card_id', flat=True)
    
    available_cards = Card.objects.filter(
        language=study_language
    ).exclude(id__in=learned_cards)
    
    if not available_cards.exists():
        return render(request, 'flashcards/complete.html')
    
    card = random.choice(available_cards)
    return render(request, 'flashcards/study.html', {'card': card})

@login_required
def check_answer(request, card_id):
    if request.method == 'POST':
        card = Card.objects.get(id=card_id)
        answer = request.POST.get('answer', '').strip()
        
        progress, created = UserProgress.objects.get_or_create(
            user=request.user,
            card=card
        )
        
        is_correct = answer.lower() == card.word.lower()
        if is_correct:
            progress.review_count += 1
            if progress.review_count >= 3:  # 连续答对3次则标记为已掌握
                progress.is_mastered = True
            progress.save()
        
        return render(request, 'flashcards/result.html', {
            'is_correct': is_correct,
            'card': card
        })

@login_required
def add_word(request):
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.user = request.user
            flashcard.save()
            messages.success(request, _('新单词添加成功！'))
            return redirect('flashcards:study')
    else:
        form = FlashcardForm()
    return render(request, 'flashcards/add_word.html', {'form': form})
