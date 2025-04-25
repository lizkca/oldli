from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from homepage import views

# 只保留语言切换的URL
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

# 所有其他URL都使用语言前缀
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('flashcards/', include('flashcards.urls', namespace='flashcards')),
    prefix_default_language=True  # 修改为True，这样默认语言也会有前缀
)

# 在开发环境中添加媒体文件的 URL 配置
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
