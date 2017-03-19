# coding=utf-8

"""
Django settings for revenge project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '83*3=)6%+vt(kr!@!wo9i5^0_75p3(0qjqafsz7zx&!5x%w=g!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

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
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    "djcelery_email",
    'kombu.transport.django',
    'bomb',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite'),
    }
}

ROOT_URLCONF = 'revenge.urls'

WSGI_APPLICATION = 'revenge.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,  'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# media files
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_DIRS = (
    ("avatars", os.path.join(MEDIA_ROOT, 'avatars')),
)

AUTH_USER_MODEL = 'auth.User'

# email
#当使用587端口时，必须开启TLS，此时使用TLS链接，不使用SSL链接；
#当使用465端口时，必须关闭TLS，此时使用SSL链接，不使用TLS链接。
#邮件服务器发送邮件只能用587端口配TLS链接。

#是否开启TLS
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.exmail.qq.com'
#邮箱服务器端口
EMAIL_PORT = 25
#登陆邮箱的用户名(必须包括域名)
EMAIL_HOST_USER = 'do_not_reply@quanttech.cn'
#登陆邮箱的密码
EMAIL_HOST_PASSWORD = 'Dnr2015'
EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
#邮箱地址
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# third party auth backends


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


import djcelery
from datetime import timedelta
djcelery.setup_loader()

CELERY_TIMEZONE = TIME_ZONE
BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_RESULT_BACKEND = 'rpc://'

CELERYBEAT_SCHEDULE = {
    'bombTaskTime-every-120-seconds':{
        'task':'bomb.tasks.bombTaskTime',
        'schedule': timedelta(seconds=1),
        'args':()
    },
}
