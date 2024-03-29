"""
Django settings for panicButton project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from decouple import config
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*i7g@d(&5^i)$l23y&8dt8p2_8ov3irhtmkbg=8&=&+xsmp2aq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DJANGO_DEBUG",default=False,cast=bool)

ALLOWED_HOSTS=['*']

CORS_ORIGIN_ALLOW_ALL = False

#CORS_ALLOW_CREDENTIALS = True
#CORS_ALLOW_ALL_ORIGINS = True

CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE =False

BASE_SOCKET_URL = config("DJANGO_URL_SOCKET",default="http://localhost:3001",cast=str)
BASE_BACKEND_URL = config("DJANGO_BASE_BACKEND_URL", default="http://localhost:8000")
BASE_FRONTEND_URL = config("DJANGO_BASE_FRONTEND_URL", default="http://localhost:3000")
CORS_ALLOWED_ORIGIN_REGEXES = [
    # Produção
    r'^https?://(\w+\.)?alertaescolar\.com$',
    # Homologação
    r'^https?://(localhost|127\.0\.0\.1)(:[3|4|5|8|9][0-9]{3})?$',
    # Additional IP and port
    r'^https?://191\.252\.185\.159:50801$',
]

SESSION_ENGINE = "django.contrib.sessions.backends.db"

# Application definition

LOCAL_APPS = [
    'apps.authentication',
    'apps.core',
    'apps.school',
    'apps.common',
    'apps.users',
    'apps.api',
    'apps.role',
    'apps.cop',
    'apps.counties',
    'apps.address',
    'apps.button',
    'apps.type_incident'
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'drf_yasg',
    'rest_framework_api_key',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "apps.api.exception_handlers.personalized_exception_handler",
     # 'EXCEPTION_HANDLER': 'apps.api.exception_handlers.drf_default_with_modifications_exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication', 
    ),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'panicButton.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'panicButton.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=config('DJANGO_DATABASE_URL',default="postgres://postgres:1234@localhost/school-alert")
    )
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = "users.BaseUser"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR,'run','static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')
MEDIA_URL='/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from config.jwt import *  # noqa
from config.doc import *  # noqa