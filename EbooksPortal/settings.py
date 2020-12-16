"""
Django settings for EbooksPortal project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n71wkc_$55i#pgw!kjd67avryy!x4k@kn!c92n=7c-epzftyk4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    'books',
    'portal',
    'papers',
    'apis',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    
    'captcha',
    
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',

    'simple_history'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'EbooksPortal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'EbooksPortal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if DEBUG:
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'EbooksPortal',
           'USER': 'EbooksPortal',
           'PASSWORD': 'portal@2',
           'HOST': 'localhost',
           'PORT': 3306,
           'OPTIONS': {
           'autocommit': True,
           },
       }
   }
else:
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'd10cgvvg9u9gob',
           'USER': 'zxcewnwvtfzupv',
           'PASSWORD': 'd2ed36477672a75cd22b5eb7a70f0c04892eaaabfa73a249c29ea0f5c4b5c0c6',
           'HOST': 'ec2-3-218-112-22.compute-1.amazonaws.com',
           'PORT': 5432,
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATICFILES_DIRS =[
    os.path.join(BASE_DIR, 'static'),
]


SITE_ID = 1


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ebooksportal.social@gmail.com'
EMAIL_HOST_PASSWORD = 'EbooksPortal@@2810'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
TO = 'lingayatajay2810@gmail.com'


RECAPTCHA_PUBLIC_KEY = '6Lef6tAZAAAAANbc_VihV-6gdEbljFWzHI_4MrAF'
RECAPTCHA_PRIVATE_KEY = '6Lef6tAZAAAAAD5Ss8kEWkp1pjdgMqEs0-kJwXbl'
RECAPTCHA_PROXY = {'http': 'http://127.0.0.1:8001'}

ACCOUNT_FORMS = {
    'signup': 'portal.forms.CustomSignUpForm',
}


ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username'
LOGIN_REDIRECT_URL = '/'


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '908927361319-t7tcdpva7lldmgd53af595csueq9ev6b.apps.googleusercontent.com',
            'secret': 'IScf7UUT1wqTrpCBxh5jAw6X',
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
   'github': {
         'APP': {
             'client_id': '84154bec7e7ddea6afa0',
             'secret': '83afebf6a0e5db72641426883b297badee559fad'
         },
         'SCOPE': [
            'user',
            'read:org',
        ],
   }
}

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}