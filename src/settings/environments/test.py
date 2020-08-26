import sys
import os
import logging

# logging.disable(logging.CRITICAL)


PROFILE = "test"
SECRET_KEY = "test_SECRET_KEY_1234"

DATABASES = {
            'default': {
                'NAME': ':memory:',
                'ENGINE': 'django.db.backends.sqlite3',
                'TEST_NAME': ':memory:',
            },
        },

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/var/tmp/django_cache",
    }
}

REDIS_CONNECT = ""

# Speed!
PASSWORD_HASHERS = ("django.contrib.auth.hashers.UnsaltedMD5PasswordHasher",)

