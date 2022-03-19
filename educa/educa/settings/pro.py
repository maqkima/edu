from .base import *

DEBUG = True

ADMINS = (
    ('admin', 'email@mydomain.com'),
)

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True

ROOT_URLCONF = 'educa.urls'

ALLOWED_HOSTS = ['educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': '456',
    }
}
