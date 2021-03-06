"""
Django settings for tabby_search project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import os
import dotenv

dotenv.load('../.env')

def env(key, default=None):
    value = dotenv.get(key, default)
    if value == 'True':
        value = True
    elif value == 'False':
        value = False
    return value

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('APP_KEY')

MODEL_KERAS_JSON = os.path.join(BASE_DIR, env('MODEL_JSON'))

MODEL_KERAS_WEIGHT = os.path.join(BASE_DIR, env('MODEL_KERAS'))

REDIS_HOST = env('REDIS_HOST')
REDIS_PORT = env('REDIS_PORT')
REDIS_DB = env('REDIS_DB')

IMAGE_WIDTH = env('IMAGE_WIDTH')
IMAGE_HEIGHT = env('IMAGE_HEIGHT')
IMAGE_CHANS = env('IMAGE_CHANS')
IMAGE_DTYPE = "float32"

IMAGE_QUEUE = env('IMAGE_QUEUE')
BATCH_SIZE = env('BATCH_SIZE')
SERVER_SLEEP = env('SERVER_SLEEP')
CLIENT_SLEEP = env('CLIENT_SLEEP')

# YOLO_CONFIG_PATH=os.path.join(BASE_DIR, env('YOLO_CONFIG_PATH'))

# YOLO_MODEL_PATH=os.path.join(BASE_DIR, env('YOLO_MODEL_PATH'))

# YOLO_MODEL_BACKEND=os.path.join(BASE_DIR, env('YOLO_MODEL_BACKEND'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('APP_DEBUG')

ADMINS = (
    (u'admin', 'admin@tabbysearch.vn'),
)

WEBSITE_NAME = "Tabby Search"

ALLOWED_HOSTS = ['*']

QUANTITATION_FACTOR=env('QUANTITATION_FACTOR')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fashion',
    'django_elasticsearch_dsl',
    'seller_images',
    'corsheaders',
    'api',
]

THUMBNAIL_HIGH_RESOLUTION = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ORIGIN_ALLOW_ALL=True

ROOT_URLCONF = 'tabby_search.urls'

ELASTICSEARCH_DSL={
    'default': {
        'hosts': 'localhost:9200'
    },
}

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
            ],
        },
    },
]

WSGI_APPLICATION = 'tabby_search.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_DATABASE'),
        'USER': env('DB_USERNAME'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ANCHOR = env('ANCHOR')
NB_CLASS = env('NB_CLASS')
OBJ_THRESHOLD = env('OBJ_THRESHOLD')
NMS_THRESHOLD = env('NMS_THRESHOLD')
LABEL = env('LABEL')
INVERSE_LABEL = env('INVERSE_LABEL')
YOLO_IMG_SIZE = env('YOLO_IMG_SIZE')

HOST_OBJ_DETECT = env('HOST_OBJ_DETECT')
PORT_OBJ_DETECT = env('PORT_OBJ_DETECT')
OBJ_DETECT_MODEL_NAME = env('OBJ_DETECT_MODEL_NAME')
BASE_PATH_OJB_DETECT_MODEL = env('BASE_PATH_OJB_DETECT_MODEL')

HOST_GET_EMB = env('HOST_GET_EMB')
PORT_GET_EMB = env('PORT_GET_EMB')
GET_EMB_MODEL_NAME = env('GET_EMB_MODEL_NAME')
BASE_PATH_GET_EMB_MODEL = env('BASE_PATH_GET_EMB_MODEL')

REQUEST_TIME_OUT_GET_EMB = 10
