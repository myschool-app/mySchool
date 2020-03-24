import os

from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
  os.path.dirname(os.path.abspath(__file__))))
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# Application definition

INSTALLED_APPS = [
  # mySchool
  'myschool_app.apps.MyschoolAppConfig',
  'utilizadores.apps.UtilizadoresConfig',
  # Aplicações PIP
  'crispy_forms',
  'django_extensions',
  # Django
  'django.contrib.admindocs',
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.locale.LocaleMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myschool.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'django.template.context_processors.i18n'
      ],
    },
  },
]

TEMPLATE_DIRS = [
  os.path.join(PROJECT_ROOT, 'templates'),
]

WSGI_APPLICATION = 'myschool.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGES = [
  ('pt-PT', _('Português')),
  ('en-US', _('Inglês')),
]

LANGUAGE_CODE = 'en-US'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Autenticação
LOGIN_REDIRECT_URL = 'app-inicio'
LOGIN_URL = 'app-login'
LOGOUT_REDIRECT_URL = 'publico-inicio'

# Tradução
LOCALE_PATHS = (
  os.path.join(BASE_DIR, 'locale'),
)
