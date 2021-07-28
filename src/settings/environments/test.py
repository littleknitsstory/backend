import os
import sys

# PROFILE = "test"
SECRET_KEY = "test_SECRET_KEY_1234"
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "TEST": {}}}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/var/tmp/django_cache",
    }
}

# REDIS_CONNECT = ""

# Speed!
PASSWORD_HASHERS = ("django.contrib.auth.hashers.UnsaltedMD5PasswordHasher",)

if "create-db" not in sys.argv:
    # and this allows you to use --reuse-db to skip re-creating the db,
    # even faster!
    SETTINGS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATABASES["default"]["TEST"]["NAME"] = f"{SETTINGS_PATH}/test.db.sqlite3"
