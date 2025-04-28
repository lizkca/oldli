from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('submit/', views.submit_feedback, name='submit'),
    path('list/', views.feedback_list, name='list'),
    path('toggle/<int:feedback_id>/', views.toggle_resolved, name='toggle_resolved'),
]