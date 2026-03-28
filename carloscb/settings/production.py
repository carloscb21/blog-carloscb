from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = get_env_var('ALLOWED_HOSTS', '').split(',')

DATABASES = {
    'default': dj_database_url.config(
        default=get_env_var('DATABASE_URL', ''),
        conn_max_age=600,
        ssl_require=True
    )
}

# Seguridad adicional para producción
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
