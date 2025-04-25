from django.urls import path
from . import views

app_name = 'speech'

urlpatterns = [
    path('', views.speech_practice, name='practice'),
]