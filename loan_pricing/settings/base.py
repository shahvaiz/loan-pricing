import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q$)^ymr=3233fghdsjghGF*&^%&5463lr+a@!997-joypgch7(js#@&h0s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # third party.
    'static_precompiler',
    'boto',
    'storages',

    # my apps.
    'myapp',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'loan_pricing.urls'

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

# Parse database configuration from $DATABASE_URL

# DATABASES['default'] =  dj_database_url.config()
DATABASES['default'] = dj_database_url.config(default='postgres://shahvaiz:pass@localhost/geodata')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
# Todo: create set up for base, local, and production.
# ALLOWED_HOSTS = ['*']

# Static asset configuration

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
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Storage on S3 settings are stored as os.environs to keep settings.py clean

if not DEBUG:
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = S3_URL
