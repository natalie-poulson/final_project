"""
Django settings for final_django project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import django_heroku


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('secret_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    # third party apps
    'social_django',
    'django_extensions',
    'crispy_forms',
    'mapwidgets',
    # my apps
    'accounts',
    'final_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # heroku
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'final_django.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ],
        },
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

WSGI_APPLICATION = 'final_django.wsgi.application'

AUTHENTICATION_BACKENDS = (
 'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
 'social_core.backends.google.GoogleOpenId',  # for Google authentication
 'social_core.backends.google.GoogleOAuth2',
 
 'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_URL ='final_app:login'
SOCIAL_AUTH_LOGIN_REDIRECT_URL ='final_app:profile'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = 'final_app:profile_create'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='1085080882765-rihjko5c4qigjjdskkjk01tg25si9sa2.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'tGfbJFHIR_PjbW1Zeiy6S0Sf' #Paste Secret Key

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['https://www.googleapis.com/auth/calendar.readonly']


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
POSTGIS_VERSION = (2, 0, 3)

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'final',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/


GOOGLE_MAP_API_KEY = "AIzaSyBHLett8djBo62dDXj0EjCimF8Rd6E8cxg"

MAP_WIDGETS = {
    "GooglePointFieldWidget": (
        ("zoom", 4),
        ("mapCenterLocation", [39.8283,  -98.5795]),
        ("markerFitZoom", 11),
    ),
    "GOOGLE_MAP_API_KEY": GOOGLE_MAP_API_KEY,
}



#The address to visit to find the media files
MEDIA_URL = '/media/'

# MEDIA_ROOT = MEDIA_DIR
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# The address to visit to find the static files 
STATIC_URL = '/static/'

# Tells Django where to find static files
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



django_heroku.settings(locals())

