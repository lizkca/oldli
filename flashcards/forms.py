from django import forms
from .models import Flashcard

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['english_word', 'chinese_translation', 'example_sentence']
        widgets = {
            'english_word': forms.TextInput(attrs={'class': 'form-control'}),
            'chinese_translation': forms.TextInput(attrs={'class': 'form-control'}),
            'example_sentence': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }