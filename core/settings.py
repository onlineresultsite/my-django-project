from pathlib import Path
import os

SECRET_KEY = 'django-insecure-r$a5(on+pbsj#o2w@ni@&#%jdf)jq@()_-ht@*@3!@wax1rnwy'
DEBUG = True
BASE_DIR = Path(__file__).resolve().parent.parent
# ------- COMMON CODE FOR HANDLE MEDIA, STATIC and TEMPLATES ---------



MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
#  --------------------------==========-------------------------------

ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'adminpanel',
    'market',
    'rest_framework',
    'django_filters',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Uncomment and configure MySQL if needed
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'chatxity',
#         'USER': 'ashiqmyi@localhost',
#         'PASSWORD': '123456@@@@@@',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

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


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


STATIC_URL = '/static/'  # Note the leading slash
STATIC_ROOT = '/home/ubuntu/my-django-project/staticfiles'

# --=====> EXTRA <=====------

AUTH_USER_MODEL = 'users.User'
LOGIN_URL = "/auth/login/"
# ------======== ------444

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
