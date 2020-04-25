"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from datetime import timedelta

from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(BASE_DIR, "templates")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool)

# Access settings
ALLOWED_HOSTS = ["*"]

# Application definition

# Application definition
DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "corsheaders",
    "debug_toolbar",
    "rest_framework",
    "rest_framework_simplejwt",
]

LOCAL_APPS = [
    'core',
    'users',
]

INSTALLED_APPS = LOCAL_APPS + THIRD_PARTY_APPS + DEFAULT_APPS

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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_PATH],
        'APP_DIRS': False,
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", default="django.db.backends.postgresql"),
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_FOLDER = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    STATIC_FOLDER,
]

# Media Configuration
MEDIA_URL = f"/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Automail SMTP Configuration
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool)
EMAIL_PORT = config("EMAIL_PORT", cast=int)
DEFAULT_FROM_EMAIL = (
    f"{config('DEFAULT_FROM_NAME')} " f"<{config('DEFAULT_FROM_EMAIL')}>"
)
TEST_EMAIL = config("TEST_EMAIL")


AUTH_USER_MODEL = "users.User"


TEST_RUNNER = "core.test_utils.MyTestSuiteRunner"


# System logs
LOG_PATH = os.path.join(BASE_DIR, "log/")
if not os.path.exists("log/"):
    os.mkdir("log/")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"testing": {"()": "core.logging_utils.NotInTestFilter"}},
    "formatters": {
        "standard": {"format": "%(asctime)s %(name)-12s [%(levelname)s]- %(message)s"}
    },
    "handlers": {
        "debug": {
            "filters": ["testing"],
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_PATH + "debug.log",
            "formatter": "standard",
        },
        "info": {
            "filters": ["testing"],
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_PATH + "info.log",
            "formatter": "standard",
        },
        "warning": {
            "filters": ["testing"],
            "level": "WARNING",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_PATH + "warning.log",
            "formatter": "standard",
        },
        "error": {
            "filters": ["testing"],
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_PATH + "error.log",
            "formatter": "standard",
        },
        "console": {
            "filters": ["testing"],
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "debug", "info", "warning", "error"],
            "propagate": True,
        },
        "core": {
            "handlers": ["console", "debug", "info", "warning", "error"],
            "level": "DEBUG",
            "propagate": False,
        }
    },
}


CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = []


INTERNAL_IPS = ["172.27.0.1", "127.0.0.1", "192.168.124.179", "localhost"]


REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination" ".PageNumberPagination",
    "PAGE_SIZE": 10,
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "core.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": [
        "url_filter.integrations.drf.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    # @TODO fix auth cookie settings
    "AUTH_COOKIE": "Authorization",
    # A string like "example.com", or None for standard domain cookie.
    "AUTH_COOKIE_DOMAIN": None,
    # Whether the auth cookies should be secure (https:// only).
    "AUTH_COOKIE_SECURE": False,
    # The path of the auth cookie.
    "AUTH_COOKIE_PATH": "/",
    # Whether to set the flag restricting cookie leaks on cross-site requests.
    # This can be 'Lax', 'Strict', or None to disable the flag.
    "AUTH_COOKIE_SAMESITE": None,
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

# @TODO fix csrf cookie settings
CSRF_COOKIE_NAME = "csrftoken"
CSRF_COOKIE_DOMAIN = None
CSRF_COOKIE_PATH = "/"
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = None
CSRF_COOKIE_SECURE = False
CSRF_HEADER_NAME = "HTTP_X_CSRFTOKEN"
CSRF_TRUSTED_ORIGINS = []
