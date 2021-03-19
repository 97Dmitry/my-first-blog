"""Django settings for test_site project.
Generated by 'django-admin startproject' using Django 3.1.3.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from django.conf import settings
from prod_settings import *
from ck_settings import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY  # os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # bool(os.getenv("DEBUG", default=False))

ALLOWED_HOSTS = ALLOWED_HOSTS.split(' ')  # os.getenv("ALLOWED_HOSTS").split(' ')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'chat.apps.ChatConfig',
    'snowpenguin.django.recaptcha3',
    'channels',
    'django.contrib.postgres',
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader',
    'corsheaders',
    'django_cleanup',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.vk'


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
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

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Channels
WSGI_APPLICATION = 'test_site.wsgi.application'
ASGI_APPLICATION = "test_site.asgi.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': POSTGRES_ENGINE,  # os.getenv("POSTGRES_ENGINE"),
        'NAME': POSTGRES_NAME,  # os.getenv("POSTGRES_NAME"),
        'USER': POSTGRES_USER,  # os.getenv("POSTGRES_USER"),
        'PASSWORD': POSTGRES_PASSWORD,  # os.getenv("POSTGRES_PASSWORD"),
        'HOST': POSTGRES_HOST,  # os.getenv("POSTGRES_HOST"),
        'PORT': POSTGRES_PORT,  # os.getenv("POSTGRES_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SHORT_DATETIME_FORMAT = 'j.m.Y H:i:s'

SHORT_DATE_FORMAT = 'j.m.Y'

TIME_FORMAT = 'H:i:s'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Cors whitelist
CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:1337",
    "http://127.0.0.1:8000",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://192.168.42.213:8080",

]

# SMTP Configurations
DEFAULT_FROM_EMAIL = 'admin@mail.com'
SERVER_EMAIL = 'admin@mail.com'
if settings.DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = EMAIL_HOST_USER  # os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD  # os.getenv("EMAIL_HOST_PASSWORD")

# URL
LOGIN_URL = 'sing_in'
LOGIN_REDIRECT_URL = '/'

# reCaptcha
RECAPTCHA_PRIVATE_KEY = PRIVATE_KEY  # os.getenv("PRIVATE_KEY")
RECAPTCHA_PUBLIC_KEY = PUBLIC_KEY  # os.getenv("PUBLIC_KEY")
RECAPTCHA_DEFAULT_ACTION = 'generic'
RECAPTCHA_SCORE_THRESHOLD = 0.5

# ckeditor

CKEDITOR_UPLOAD_PATH = CKEDITOR_UPLOAD_PATH
CKEDITOR_CONFIGS = CKEDITOR_CONFIGS

SITE_ID = 4
