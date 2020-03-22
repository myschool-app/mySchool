from .base import *
from sentry_sdk.integrations.django import DjangoIntegration
import dj_database_url


DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com', ]

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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myschool',
        'USER': 'postgres',
        'PASSWORD': 'afonso123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

sentry_sdk.init(
    dsn="https://0c67ef81471f46b59a99e4921e1d1775@sentry.io/3966168",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True
)

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
