from .base import *

DEBUG = False
ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your-db-name',
        'USER': 'your-db-user-name',
        'PASSWORD': 'db-password',
        'HOST': 'localhost',
        'PORT': ''
    }
}

STRIPE_PUBLIC_KEY = 'your-live-public-key'
STRIPE_SECRET_KEY = 'your-live-secret-key'
