from decouple import config
from split_settings.tools import include

CONFIG_NAME = config("ENVIRONMENT", "test") # "development"

base_settings = [
    "components/_paths.py",
    "components/apps.py",
    "components/cache.py",
    "components/ckeditor.py",
    "components/common.py",
    "components/cors.py",
    "components/database.py",
    "components/emails.py",
    "components/logging.py",
    "components/*.py",
    # Select the right env:
    f"environments/{CONFIG_NAME}.py",
]

# Include settings:
include(*base_settings)
