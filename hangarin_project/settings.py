import os
import socket
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-hii^l-+m7kjdeooddk(8tc!ti5r!e#e4a7&i_4$hb9$26fc0e='

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'steigmeistertr.pythonanywhere.com']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',
    'widget_tweaks',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'pwa',
]

if os.environ.get('PYTHONANYWHERE_SITE') == 'steigmeistertr.pythonanywhere.com':
    SITE_ID = 2 # production site
else:
    # Fallback: Check hostname, but this might be unreliable on PA
    # A more robust check might be needed depending on PA's internal hostname structure
    hostname = socket.gethostname()
    # You might need to adjust this check based on the actual hostname seen on your PA account
    # Common patterns might be like 'steigmeistertr-web-...' or just 'webXX'
    # For now, let's try a more general check that might work
    if 'steigmeistertr' in hostname and 'pythonanywhere' in hostname:
        SITE_ID = 2 # production site
    else:
        SITE_ID = 3 # local site (or other non-production)

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hangarin_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'templates'))],
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

WSGI_APPLICATION = 'hangarin_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL='/accounts/login/'
LOGIN_REDIRECT_URL='/'
LOGOUT_REDIRECT_URL='/accounts/login/'

ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_ON_GET = True

ACCOUNT_LOGIN_METHODS = {'username', 'email'}

ACCOUNT_SIGNUP_FIELDS = [
    'username*',
    'email*',
    'password1*',
    'password2*',
]

# --- Progressive Web App Settings ---
PWA_APP_NAME = 'ProjectSite'
PWA_APP_DESCRIPTION = "A Progressive Web App version of ProjectSite"
PWA_APP_THEME_COLOR = '#0A0A0A'
PWA_APP_BACKGROUND_COLOR = '#FFFFFF'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'portrait'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
{
'src': '/static/img/icon-192.png',
'sizes': '192x192'
},
{
'src': '/static/img/icon-512.png',
'sizes': '512x512'
}
]
PWA_APP_ICONS_APPLE = [
{
'src': '/static/img/icon-192.png',
'sizes': '192x192'
},
{
'src': '/static/img/icon-512.png',
'sizes': '512x512'
}
]
PWA_APP_DIR = 'ltr'
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js', 'serviceworker.js')
