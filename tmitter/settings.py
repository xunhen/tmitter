"""
Django settings for tmitter project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l5k835%!2980&xthzq96^=_67!=-h_q1k4($!^q=g2ap*z^e!8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tmitter_web',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',   #国际化
]

ROOT_URLCONF = 'tmitter.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'tmitter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

ugettext = lambda s: s

LANGUAGES = (
  ('zh-cn', u'简体中文'),
  ('en', u'English'),
)

DEFAULT_CHARSET = "utf-8"

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'conf', 'locale'),
)

SITE_ID = 1

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '%s/static/uploads/' % BASE_DIR

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/static/uploads/'

# Default user face
DEFAULT_FACE = '/static/images/face%d.png'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

CACHE_BACKEND = 'locmem:///'

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
# DATABASE_NAME = '%s/db/tmitter.sqlite' % BASE_DIR          # Or path to database file if using sqlite3.
# DATABASE_USER = ''             # Not used with sqlite3.
# DATABASE_PASSWORD = ''         # Not used with sqlite3.
# DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
# DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'


# 网站信息设置
APP_DOMAIN = 'http://127.0.0.1:8080/'
APP_NAME = 'Tmitter'
APP_VERSION = '0.2.9'
APP_COMPANY = 'Thewolfs Team'
APP_LICENSE = 'GNU General Public License v2'

# 全局分页的每页条数
PAGE_SIZE = 4
# 管理后台列表每页条数
ADMIN_PAGE_SIZE = 20

# 网友空间的好友列表个数限制
FRIEND_LIST_MAX = 10

# Feed 相关的设置
FEED_ITEM_MAX = 20

# Email 服务器设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False   #是否使用TLS安全传输协议(用于在两个通信应用程序之间提供保密性和数据完整性。)
EMAIL_USE_SSL = True    #是否使用SSL加密，qq企业邮箱要求使用
EMAIL_HOST = 'smtp.163.com'  #发送邮件的邮箱 的 SMTP服务器，这里用了163邮箱
EMAIL_PORT = 465     #发件箱的SMTP服务器端口--这里SSL加密，本来是25
EMAIL_HOST_PASSWORD = 'xy12345'
EMAIL_HOST_USER = '17816877003@163.com'#发送邮件的邮箱地址
EMAIL_SUBJECT_PREFIX = '[Tmitter]'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2', #'django.db.backends.',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'tmitter',  # Or path to database file if using sqlite3.
#         'USER': 'postgres',  # Not used with sqlite3.
#         'PASSWORD': 'postgres',  # Not used with sqlite3.
#         'HOST': '127.0.0.1',  # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '5432',  # Set to empty string for default. Not used with sqlite3.
#     }
# }
