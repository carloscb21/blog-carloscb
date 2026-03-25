from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_env_var('DB_NAME', 'dev'),
        'USER': get_env_var('DB_USER', 'admin'),
        'PASSWORD': get_env_var('DB_PASSWORD', 'admin_milan_21_2345'),
        'HOST': get_env_var('DB_HOST', 'localhost'),
        'PORT': get_env_var('DB_PORT', '5432'),
    }
}
