from django.shortcuts import render
from django.contrib.auth import get_user_model

def index(request):
    User = get_user_model()
    user_count = User.objects.count()
    return render(request, 'homepage/index.html', {
        'user_count': user_count
    })