"""
Django settings for CAPSTONE_PROJECT project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Google API Key for Gemini
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

ALLOWED_HOSTS = ['192.168.1.4', 'localhost', '127.0.0.1', '192.168.0.14', '192.168.135.71', '192.168.254.118', '192.168.134.71', '192.168.1.10', '192.168.254.140', '192.168.1.6','*']




# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "traffic_violation_system",
    "traffic_violation_system.educational.apps.EducationalConfig",
    "sslserver",
    "django_extensions",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'traffic_violation_system.middleware.AuthenticationMiddleware',
    'traffic_violation_system.middleware.NoCacheMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = "CAPSTONE_PROJECT.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'traffic_violation_system.context_processors.user_notifications',
            ],
        },
    },
]
WSGI_APPLICATION = "CAPSTONE_PROJECT.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'capstone',
        'USER': 'root',
        'PASSWORD': '',  # If you have a password, put it here
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
            'use_unicode': True,
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / 'static'

# Replace Stripe settings with Paymongo


# Update these settings
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

# Session and Security Settings
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 3600  # 1 hour in seconds
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_SECURE = False  # Changed to False to work with both HTTP and HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'  # Changed from 'Strict' to 'Lax' for better compatibility

# Security Settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Cache settings
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 300,  # 5 minutes
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

# Cache middleware settings
CACHE_MIDDLEWARE_SECONDS = 0  # Don't cache pages
CACHE_MIDDLEWARE_KEY_PREFIX = ''

# Mobile-specific settings
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False  # Changed to False to work with both HTTP and HTTPS

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CSRF_TRUSTED_ORIGINS = ['https://api.paymongo.com']

# Add these settings if they're not already present
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Delete duplicate INSTALLED_APPS declaration (already defined above)

STRIPE_PUBLIC_KEY = 'pk_test_51QMUtiRtsOGIIsiiixsia2aXfEA3K3aWdsxOUP70JIVEqoBPOOTRqfG0rzuhvokcNBIwZJQV5TTwmI6EM2UFAquf00l1UPS9oo'
STRIPE_SECRET_KEY = 'sk_test_51QMUtiRtsOGIIsii5FbSeuUGHw5rhyUaVkIJfAVA8UbqHpW4YRTm7BjIftFB34UQC7G1sqqVQrdpTo9b2YadUjcQ00I21Bdd4g'
PAYPAL_CLIENT_ID = 'AeBk0i0IG66r6i0kFzphzpKjAekDL5WUS-fBRR8KSTFNr4HEQjiviJTdFEvX1Hy13jElkjiGdJ4OQe-W'
PAYPAL_CLIENT_SECRET = 'yEPApFknBCa218RIXGFHVZU7QdFfeZFGHp53QVw79ZblnBVpUl3wqqbf81SxDI0tO7FdsVDGHNoYK0dFA'

# PayMongo API Keys
PAYMONGO_PUBLIC_KEY = 'pk_test_yourpaymongokeypublicvalue'
PAYMONGO_SECRET_KEY = 'sk_test_yourpaymongosecretkeyvalue'

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# Update CORS settings to allow frontend requests
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]