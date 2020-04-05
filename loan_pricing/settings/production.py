import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# The base dir is where the mange.py file is at.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@!-)jwmuzh8btr380g61=g+#&zzei&dz2(&=xbvxztady)_p(r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', 'one-click-project.herokuapp.com']

# Running code api
CLIENT_ID = '8acba1648460ab5cc5e502f507d3230e'
CLIENT_SECRET = '6ca2d92b2a297ad77ddd01da8f73f39228f07b4fdee1bb5dfbd0f90d517cb64b'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party library.
    'bootstrap_datepicker_plus',
    'bootstrap4',
    'storages',

    # our apps
    'accounts',
    'addresses',
    'analytics',
    'billing',
    'carts',
    'marketing',
    'orders',
    'products',
    'search',
    'tags',
    'teachers',
    'students',
    'classes',
    'questions',
    'tests',
    'projects',
    'sections',
    'schedule',
    'test_answers',
    'run_code',
    'student_tests',
    'tests_statistics',
    'tests_progress',
    'student_projects',
    'project_answers',
    'student_tests_statistics',
    'projects_statistics',
    'projects_partial_credit',
    'tests_partial_credit',
]

AUTH_USER_MODEL = 'accounts.User'  # changes the built-in user model to ours


FORCE_SESSION_TO_ONE = False
FORCE_INACTIVE_USER_ENDSESSION = False

LOGIN_URL = '/login/'
LOGIN_URL_REDIRECT = '/'
LOGOUT_URL = '/logout/'

MAILCHIMP_API_KEY           = "0942f9e17f5f7b3e6ee87661da138071-us19"
MAILCHIMP_DATA_CENTER       = 'us19'
MAILCHIMP_EMAIL_LIST_ID     = 'b115f21888'

STRIPE_SECRET_KEY = "sk_test_Fka4oAAs9n7P470v5e2WEgdp"
STRIPE_PUB_KEY = 'pk_test_FGYKpKGuPaPCMLECCQB9zMFD'

BASE_URL = 'https://oneclick.com'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LOGOUT_REDIRECT_URL = '/login/'
ROOT_URLCONF = 'one_click.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'one_click.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
    }
}


db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "static_root")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_my_proj"),
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "media_root")

PROTECTED_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "protracted_media")

from one_click.aws.conf import *

# This settings is very important for the project because we need to make sure that our site is https. That is, safe.
CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True
