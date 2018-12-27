import os
from decouple import config
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/

SECRET_KEY = config('SECRET_KEY')
SITE_ID = 1

PAGINATION_BY = 6

DEBUG = True
ALLOWED_HOSTS = ['*']
LOGIN_REDIRECT_URL = 'dashboard:list'

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'webpack_loader',
    'django_extensions',
    'django_mptt_admin',
    'mptt',
    # 'modeltranslation',
    'social_django',
    'captcha',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'ckeditor',
    'ckeditor_uploader',
    'rest_framework_swagger',
    'optimized_image',
    'phonenumber_field',
    'djmoney',
    # 'threadedcomments',
    'fluent_comments',  # must be before django_comments
    'crispy_forms',
    'django_comments',
    # Apps project
    'apps.blog',
    'apps.tags',
    'apps.shop',
    'apps.menu',
    'apps.users',
    'apps.contacts',
    'apps.dashboard',
    'apps.slider',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]


AUTHENTICATION_BACKENDS = (
    'social_core.backends.email.EmailAuth',
    'social_core.backends.vk.VKOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_USER_MODEL = 'users.User'
USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

CSRF_COOKIE_NAME = "XCSRF-Token"

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = ['*']

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates/', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#
# MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
#

gettext = lambda s: s  # noqa

LANGUAGES = (
    ('ru', gettext('Russian')),
    ('en', gettext('English')),
)

LOCALE_PATHS = (
    ROOT_DIR + '/apps/locale', )


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '../storage/static')
STATICFILES_DIRS = (os.path.join(ROOT_DIR, 'static'),)

MEDIA_URL = '/storage/'
MEDIA_ROOT = os.path.join(ROOT_DIR, '../storage/media')

PHONE_REGEX = r'^(\+7)+([0-9]){10}$'
PHONE_VALIDATOR = RegexValidator(regex=PHONE_REGEX,
                                 message=_('Enter the number in the format +79991234567.'))

OPTIMIZED_IMAGE_METHOD = 'pillow'
