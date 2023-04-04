from decouple import config
from split_settings.tools import include

CONFIG_NAME = config("ENVIRONMENT", "test")

base_settings = [
    "components/_paths.py",
    "components/*.py",
    # Select the right env:
    f"environments/{CONFIG_NAME}.py",
]

# Include settings:
include(*base_settings)
