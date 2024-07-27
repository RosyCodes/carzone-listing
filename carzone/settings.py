"""
Django settings for carzone project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from django.contrib.messages import constants as messages
import os

# we add this block for HERUKU deployment
import dj_database_url
import django_heroku
# from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '79wc33dl6fo^co%2d%@2@vq%a6k8_5er=@(vxi=383!g%$re$u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# redirects to the dashboard after verified social media login
LOGIN_REDIRECT_URL = 'dashboard'

# immediately redirects to the social media login page
SOCIALACCOUNT_LOGIN_ON_GET = True

# Application definition

INSTALLED_APPS = [
    'contacts.apps.ContactsConfig',
    'accounts.apps.AccountsConfig',
    'cars.apps.CarsConfig',
    'pages.apps.PagesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'django.contrib.humanize',
    # for social media logins
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # # social media providers
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.linkedin_oauth2',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # allauth account middleware for social login
    'allauth.account.middleware.AccountMiddleware',
    # for HEROKU deployment
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'carzone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # this is the folder in the root or base directory for our web pages
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'carzone.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


# # we add this block for HERUKU deployment
# DATABASE_URL is in our ENV file
DATABASES = {'default': dj_database_url.config(
    default='postgres://postgres:adminRosy@localhost:5434/carzone_db')}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


# STATIC FILE CONFIGURATON
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'carzone/static'),
]

# MEDIA FILE CONFIGURATION
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# CUSTOMIZED MESSAGES CONFIGURATION

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# SOCIAL MEDIA CONFIGURATION
SITE_ID = 1


# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# ]

SOCIALACCOUNT_PROVIDERS = {

}

# EMAIL CONFIGURATION
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Email Setup
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rosy61625@gmail.com'
EMAIL_HOST_PASSWORD = 'xmkamjunbsjvvipt'
EMAIL_USE_TLS = True

# Whitenoise Configuration for HEROKU deployment
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
django_heroku.settings(locals())

WHITENOISE_MANIFEST_STRICT = False
