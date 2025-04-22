MIDDLEWARE = [
    # ... existing code ...
    'django.middleware.locale.LocaleMiddleware',
    # ... existing code ...
]

LANGUAGES = [
    ('en', 'English'),
    ('zh-hans', '简体中文'),
    # 添加你需要支持的其他语言
]

USE_I18N = True
USE_L10N = True