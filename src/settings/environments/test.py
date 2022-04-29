import os
import sys

from src.settings.components._paths import BASE_DIR

SECRET_KEY = "test_SECRET_KEY_1234"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        "TEST": {}
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/var/tmp/django_cache",
    }
}

REDIS_CONNECT = ""

# Speed!
PASSWORD_HASHERS = ("django.contrib.auth.hashers.UnsaltedMD5PasswordHasher",)

if "create-db" not in sys.argv:
    # and this allows you to use --reuse-db to skip re-creating the db,
    # even faster!

    # Database
    # https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
    DATABASES["default"]["TEST"]["NAME"] = f"{BASE_DIR}/test.db.sqlite3"
