import os
from travelers_project import local_settings
from celery.schedules import crontab


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEBUG = local_settings.DEBUG
THUMBNAIL_DEBUG = local_settings.THUMBNAIL_DEBUG

ALLOWED_HOSTS = ['lifeinpenza.fvds.ru', 'russiantravel.net', '127.0.0.1', '91.240.85.84']

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
    'django_celery_beat',

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
    'trips',
    'mainpage',
    'vk_poster',
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
                'travelers.context_processors.get_facebook_url',
                'travelers.context_processors.get_vk_url',
                'travelers.context_processors.get_instagram_url',
                'travelers.context_processors.get_num_of_travelers',
                'travelers.context_processors.get_num_of_completed_trips',
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

LANGUAGE_CODE = 'ru-ru'

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

VK_GROUP_ID = local_settings.VK_GROUP_ID
VK_TOKEN = local_settings.VK_TOKEN
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

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_BEAT_SCHEDULE = {
    'post-every-minute': {
        'task': 'geography.tasks.post',
        'schedule': crontab(minute='*/1'),
    }
}
