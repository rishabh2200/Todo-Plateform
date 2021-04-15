from backend.settings.base import *
import os 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('db_path'),
        'PORT': 5432,
    }
}
DEBUG = True

ALLOWED_HOSTS = ['*']