from decouple import config

SECRET_KEY = config("SECRET_KEY", "BAD_SECRET_KEY_73812732478324783274823")
AUTH_USER_MODEL = "account.User"

PAGINATION_BY = 6

DEBUG = True
ALLOWED_HOSTS = ["*"]

CSRF_COOKIE_NAME = "XCSRF-Token"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


OPTIMIZED_IMAGE_METHOD = "pillow"

SIGN_OUT_REDIRECT_URL = "https://littleknitsstory.com"
