import os

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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # Add this line
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]