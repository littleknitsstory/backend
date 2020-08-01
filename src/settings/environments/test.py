import sys
import os
import logging

logging.disable(logging.CRITICAL)


PROFILE = "test"
SECRET_KEY = "test_SECRET_KEY_1234"
DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:", "TEST": {}}
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/var/tmp/django_cache",
    }
}

# # Use in-memory file storage
# DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'

# Speed!
PASSWORD_HASHERS = ("django.contrib.auth.hashers.UnsaltedMD5PasswordHasher",)


# # Fake out migrations to speed up tests
# class DisableMigrations(object):
#     def __contains__(self, item):
#         return True
#
#     def __getitem__(self, item):
#         return None


# MIGRATION_MODULES = DisableMigrations()


if not "create-db" in sys.argv:
    # and this allows you to use --reuse-db to skip re-creating the db,
    # even faster!
    SETTINGS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATABASES["default"]["TEST"]["NAME"] = f"{SETTINGS_PATH}/test.db.sqlite3"

from src.core.conftest import *
print('test2')
