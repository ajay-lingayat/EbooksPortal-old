from .base import *


INSTALLED_APPS += [
    'captcha',
    
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',

    'simple_history',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
]


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
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
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
   'github': {
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