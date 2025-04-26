from django.urls import path
from . import views

app_name = 'homepage'  # 添加这行

urlpatterns = [
    path('', views.index, name='index'),
]