from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include

urlpatterns = [
    # ... existing code ...
    path('i18n/', include('django.conf.urls.i18n')),
    # ... existing code ...
]