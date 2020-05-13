import os

from split_settings.tools import include

SETTINGS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
include(
    f'{SETTINGS_PATH}/components/_paths.py',
    f'{SETTINGS_PATH}/components/*.py'
)

PROFILE = 'test'

from decouple import config

SECRET_KEY = 'test_SECRET_KEY_1234'
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("POSTGRES_DB", "POSTGRES_DB"),
        "USER": config("POSTGRES_USER", "POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD", "POSTGRES_PASSWORD"),
        "HOST": config("POSTGRES_HOST", "postgresql"),
        "PORT": config("POSTGRES_PORT", 5432),
    }
}
