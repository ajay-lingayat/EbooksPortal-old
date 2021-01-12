from .base import *


if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_DATA = get_secret('EMAIL')
    EMAIL_BACKEND = get_secret('BACKEND', secrets=EMAIL_DATA)
    EMAIL_HOST_USER = get_secret('USER', secrets=EMAIL_DATA)
    EMAIL_HOST_PASSWORD = get_secret('PASSWORD', secrets=EMAIL_DATA)
    EMAIL_HOST = get_secret('HOST', secrets=EMAIL_DATA)
    EMAIL_PORT = get_secret('PORT', secrets=EMAIL_DATA)
    EMAIL_USE_TLS = get_secret('USE_TLS', secrets=EMAIL_DATA)
    EMAIL_USE_SSL = get_secret('USE_SSL', secrets=EMAIL_DATA)
    TO = get_secret('TO', secrets=EMAIL_DATA)


REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_VERSION' : 'v1',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}