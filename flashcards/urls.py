from django.urls import path
from . import views

app_name = 'flashcards'

urlpatterns = [
    path('', views.study, name='study'),
    path('check/<int:card_id>/', views.check_answer, name='check_answer'),
    path('add/', views.add_word, name='add_word'),
]