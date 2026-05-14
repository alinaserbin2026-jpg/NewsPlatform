import os
from pathlib import Path
from dotenv import load_dotenv
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')


SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-if-not-found')
DEBUG = os.getenv('DEBUG', 'True') == 'True'
raw_hosts = os.getenv('ALLOWED_HOSTS', 'localhost')
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS=[os.getenv('CSRF_TRUSTED_ORIGINS', 'https://localhost')]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}
INSTALLED_APPS = [
    'unfold',
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'django.contrib.admin',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    'invitations',
    'django.contrib.sites',
    'ckeditor',
    'ckeditor_uploader',

    'rest_framework',
    'drf_spectacular',
    # 'corsheaders',

    'users',
    # 'content',
]
SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "optional"
INVITATIONS_SIGNUP_REDIRECT = "account_signup"
INVITATIONS_LOGIN_REDIRECT = "account_login"

# --- MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = '/admin/'

# --- UNFOLD НАСТРОЙКИ ---
UNFOLD = {
    "SITE_TITLE": "News Project Admin",
    "SITE_HEADER": "Project Management",
    "SITE_URL": "/",

    "STYLES": [
        "https://cdn.tailwindcss.com",  # Просто строка без lambda
    ],
    "SCRIPTS": [
        "https://unpkg.com/@phosphor-icons/web",  # Просто строка без lambda
    ],
    "COLORS": {
        "primary": {
            "50": "250 245 255", "100": "243 232 255", "200": "233 213 255",
            "300": "216 180 254", "400": "192 132 252", "500": "168 85 247",
            "600": "147 51 234", "700": "126 34 206", "800": "107 33 168",
            "900": "88 28 135", "950": "59 7 100",
        },
    },
    "SIDEBAR": {
    "show_search": True,
    "show_all_applications": False, # Скроем лишний стандартный мусор Django
    "navigation": [
        {
            "title": _("User Management"),
            "items": [
                {
                    "title": _("Users"),
                    "icon": "people",
                    "link": reverse_lazy("admin:users_user_changelist"),
                },
            ],
        },
#         {
#             "title": _("Media Archive"),
#             "items": [
#                 {
#                     "title": _("Media Library"),
#                     "link": reverse_lazy("admin:content_multimedia_changelist"), # Сделали динамической
#                     "icon": "perm_media"
#                 },
#             ],
#         },
#         {
#             "title": _("Content Management"),
#             "items": [
#                 {"title": _("News"), "link": reverse_lazy("admin:content_news_changelist"), "icon": "article"},
#                 {"title": _("Shows"), "link": reverse_lazy("admin:content_show_changelist"), "icon": "live_tv"},
#                 {"title": _("Promos"), "link": reverse_lazy("admin:content_promo_changelist"), "icon": "campaign"},
# {"title": _("Shorts"), "link": reverse_lazy("admin:content_short_changelist"), "icon": "video_library"},
#             ],
#         },
    ],
},
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- REST FRAMEWORK & SPECTACULAR ---
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'News Project API',
    'DESCRIPTION': 'API для управления пользователями и инвайтами',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

INVITATIONS_INVITATION_ONLY = True
INVITATIONS_GONE_ON_ACCEPT_ERROR = False
INVITATIONS_LOGIN_REDIRECT = '/admin/login/'

# --- DATABASE ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# --- AUTH ---
AUTH_USER_MODEL = 'users.User'
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', '')
WSGI_APPLICATION = 'core.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'backend' / 'media'
CORS_ALLOW_ALL_ORIGINS = True
STATICFILES_DIRS = [
    BASE_DIR / 'assets',
]
STATIC_ROOT = BASE_DIR / 'static'
CELERY_BROKER_URL = os.getenv('REDIS_URL')
CELERY_RESULT_BACKEND = os.getenv('REDIS_URL')
CKEDITOR_EXTERNAL_PLUGINS = [
    ('youtube', os.path.join(STATIC_URL, 'ckeditor/ckeditor/plugins/youtube/plugin.js')),
]

# 2. Настраиваем сам редактор
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Youtube', 'Table', 'HorizontalRule', 'SpecialChar'], # Youtube тут!
            ['Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'Source'],
        ],
        'height': 450,
        'width': '100%',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',
            'div',
            'autolink',
            'youtube',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
        ]),
    },
}