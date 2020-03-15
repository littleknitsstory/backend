from split_settings.tools import optional, include
from decouple import config

CONFIG_NAME = config("DJANGO_ENV") or "development"

base_settings = [
    "components/common.py",  # standard django settings
    "components/database.py",  # postgres
    # 'components/social.py',  # social auth
    "components/emails.py",  # emails
    "components/logger.py",  # logging
    "components/ckeditor.py",  # ckeditor
    "components/cache.py",  # config django-redis
    "components/*.py",
    # Select the right env:
    "environments/%s.py" % CONFIG_NAME,
    # Optionally override some settings:
    optional("environments/local.py"),
]

# Include settings:
include(*base_settings)
