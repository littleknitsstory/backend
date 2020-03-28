from split_settings.tools import optional, include
from decouple import config

CONFIG_NAME = config("DJANGO_ENV") or "development"

base_settings = [
    "components/_path.py",  # standard django settings
    "components/apps.py",  # standard django settings
    "components/cache.py",  # standard django settings
    "components/ckeditor.py",  # standard django settings
    "components/common.py",  # standard django settings
    'components/cors.py',  # social auth
    "components/database.py",  # postgres
    "components/emails.py",  # emails
    "components/logger.py",  # logging
    "components/*.py",
    # Select the right env:
    "environments/%s.py" % CONFIG_NAME,
    # Optionally override some settings:
    optional("environments/local.py"),
]

# Include settings:
include(*base_settings)
