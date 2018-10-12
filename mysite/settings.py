"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""


import sys
#sys.path.append('/Users/shahvaiz/sites/potomac_rates_calculation/potomac_rates_calculation')
#sys.path.append('https://github.com/shahvaiz/potomac_rates_calculation/potomac_rates_calculation/')


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#http://stackoverflow.com/questions/6367014/how-to-send-email-via-django
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'support@buckinghamfg.com'
#EMAIL_HOST_PASSWORD = 'maryland74'
EMAIL_HOST_USER = 'support@bfgusa.com'
EMAIL_HOST_PASSWORD = 'maryland20'
#EMAIL_HOST_PASSWORD = os.environ['EMAILPW']
EMAIL_PORT = 587

#comment this line when pushing to production; uncomment when testing locally
#SSLIFY_DISABLE = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q$)^ymr=+w9qe4ih8_!4xezlr+a@!997-joypgch7(js#@&h0s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#TEMPLATE_DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') # SSL Cert

# Application definition

#EMAIL_HOST_PASSWORD = os.environ['MY_PASSWORD_THAT_YOU_CANT_KNOW']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'storages',
    'boto',
    #'south',
    'static_precompiler',
    'django.contrib.humanize',
)

MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

#WSGI_APPLICATION = 'myapp.wsgi.application'

GOOGLE_RECAPTCHA_SECRET_KEY = '6LdjOmYUAAAAAL0N_f3qpDKtldLuvydgzsWo1rWb'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg22",
        "NAME": "geodata",
        "USER": "shahvaiz",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Parse database configuration from $DATABASE_URL
import dj_database_url
#DATABASES['default'] =  dj_database_url.config()
DATABASES['default'] =  dj_database_url.config(default='postgres://shahvaiz:pass@localhost/geodata')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = ''
STATIC_ROOT = os.path.join('myapp', 'static')
STATIC_URL = '/static/'




STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
)
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SETTINGS_PATH, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

#Storage on S3 settings are stored as os.environs to keep settings.py clean

if not DEBUG:
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = S3_URL
