import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # src/
ROOT_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)  # root/

SECRET_KEY = config("SECRET_KEY")
# SITE_ID = 1
AUTH_USER_MODEL = "account.User"

PAGINATION_BY = 6

DEBUG = True
ALLOWED_HOSTS = ["*"]

CSRF_COOKIE_NAME = "XCSRF-Token"
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
]
ROOT_URLCONF = "src.core.urls"
WSGI_APPLICATION = "src.core.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(ROOT_DIR, "static")
# STATICFILES_DIRS = (os.path.join(ROOT_DIR, 'static'),)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(ROOT_DIR, "media")

OPTIMIZED_IMAGE_METHOD = "pillow"
FORMAT_TZ = "%m/%d/%Y, %H:%M:%S"
