from .dev import *


INSTALLED_APPS += [
    'whitenoise.runserver_nostatic'
]


MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]