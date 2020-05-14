import sys
import os
from split_settings.tools import include
# Disable logging
import logging
logging.disable(logging.CRITICAL)
logging.disable(logging.WARNING)


SETTINGS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
include(
    f'{SETTINGS_PATH}/components/*.py',
)

PROFILE = 'test'
SECRET_KEY = 'test_SECRET_KEY_1234'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'TEST': {}
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}


# # Use in-memory file storage
# DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'

# Speed!
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
)


# Fake out migrations to speed up tests
class DisableMigrations(object):
    
    def __contains__(self, item):
        return True
    
    def __getitem__(self, item):
        return None
    
    
MIGRATION_MODULES = DisableMigrations()


if not 'create-db' in sys.argv:
    # and this allows you to use --reuse-db to skip re-creating the db,
    # even faster!
    #
    # To create the RAMDisk, use bash:
    # $ hdiutil attach -nomount ram://$((2 * 1024 * SIZE_IN_MB))
    # /dev/disk2
    # $ diskutil eraseVolume HFS+ RAMDisk /dev/disk2
    DATABASES['default']['TEST']['NAME'] = f'{SETTINGS_PATH}/test.db.sqlite3'
