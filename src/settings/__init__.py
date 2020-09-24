from split_settings.tools import optional, include
from decouple import config

CONFIG_NAME = config("DJANGO_ENV", "test") or "development"
print(CONFIG_NAME)

base_settings = [
    "components/_paths.py",  # standard django settings
    "components/apps.py",  # standard django settings
    "components/cache.py",  # standard django settings
    "components/ckeditor.py",  # standard django settings
    "components/common.py",  # standard django settings
    "components/cors.py",  # social auth
    "components/database.py",  # postgres
    "components/emails.py",  # emails
    "components/logging.py",  # logging
    "components/*.py",
    # Select the right env:
    f"environments/{CONFIG_NAME}.py",
]

# Include settings:
include(*base_settings)
