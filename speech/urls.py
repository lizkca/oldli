from django.urls import path
from . import views

app_name = 'speech'  # Add this line

urlpatterns = [
    path('', views.speech_practice, name='practice'),
    path('delete_record/<int:record_id>/', views.delete_record, name='delete_record'),
]