import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEBUG = True
THUMBNAIL_DEBUG = False

ALLOWED_HOSTS = ['lifeinpenza.fvds.ru', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'sorl.thumbnail',
    'django_extensions',
    'graphene_django',

    # own apps
    'geography',
    'graphql_api',
    'laboratory',
    'travelers',
    'traces',
    'vkapp',
    'autotraveler_parser',
    'instaposter',
    'feedback',
]

if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'travelers_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'travelers.context_processors.get_vars',
            ],
        },
    },
]

INTERNAL_IPS = ['127.0.0.1']

GRAPHENE = {
    'SCHEMA': 'travelers_project.schema.schema'
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],

    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}

SWAGGER_SETTINGS = {
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
}

WSGI_APPLICATION = 'travelers_project.wsgi.application'

from travelers_project import local_settings

DATABASES = local_settings.DATABASES
SECRET_KEY = local_settings.SECRET_KEY

AUTH_PASSWORD_VALIDATORS = [
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_PHOTO_PATH = os.path.join(MEDIA_ROOT, 'images', 'not-foto.png')

VK_TOKEN = local_settings.token
VK_APP_ID = local_settings.VK_APP_ID
VK_LOGIN = local_settings.VK_LOGIN
VK_PASSWORD = local_settings.VK_PASSWORD
VK_API_VERSION = local_settings.VK_API_VERSION
YMAPS_KEY = local_settings.YMAPS_KEY

INST_USERNAME = local_settings.INST_USERNAME
INST_PASSWORD = local_settings.INST_PASSWORD

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = local_settings.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = local_settings.EMAIL_HOST_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True

PAGINATION_COUNT_ONE = 60
