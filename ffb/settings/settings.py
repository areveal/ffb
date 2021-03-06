"""
Django settings for ffb project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*!_7u2lno^ruhv=axros63f@(hakr1)!5d+$wv*&$h!o-v4(6!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'fabric',

)

LOCAL_APPS = (
    'ffb.leagues',
    'ffb.players',
    'ffb.teams',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'ffb.urls'

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

WSGI_APPLICATION = 'ffb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'local_ffb_test_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


#Positions
QUARTERBACK = 'QB'
RUNNING_BACK = 'RB'
WIDE_RECEIVER = 'WR'
TIGHT_END = 'TE'
FULL_BACK = 'FB'
FREE_SAFETY = 'FS'
KICKER = 'K'
PUNTER = 'P'
DEFENSIVE_TACKLE = 'DT'
OUTSIDE_LINEBACKER = 'OLB'
DEFENSIVE_END = 'DE'
DEFENSIVE_BACK = 'DB'
STRONG_SAFETY = 'SS'
MIDDLE_LINEBACKER = 'MLB'
CORNER_BACK = 'CB'
TACKLE = 'T'
LINEBACKER = 'LB'
INSIDE_LINEBACKER = 'ILB'
NOSE_TACKLE = 'NT'
GUARD = 'G'

POSITIONS = (
    (QUARTERBACK, "uarterback"),
    (RUNNING_BACK, "running back"),
    (WIDE_RECEIVER, 'wide receiver'),
    (TIGHT_END, 'tight end'),
    (FULL_BACK, 'full back'),
    (FREE_SAFETY, 'free safety'),
    (KICKER, 'kicker'),
    (PUNTER, 'punter'),
    (DEFENSIVE_TACKLE, 'defensive tackle'),
    (OUTSIDE_LINEBACKER, 'outside linebacker'),
    (DEFENSIVE_END, 'defensive end'),
    (DEFENSIVE_BACK, 'defensive back'),
    (STRONG_SAFETY, 'strong safety'),
    (MIDDLE_LINEBACKER, 'middle linebacker'),
    (CORNER_BACK, 'corner back'),
    (TACKLE, 'tackle'),
    (LINEBACKER, 'linebacker'),
    (INSIDE_LINEBACKER, 'inside linebacker'),
    (NOSE_TACKLE, 'nose tackle'),
    (GUARD, 'guard')
)
