import os

from split_settings.tools import include

SETTINGS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
include(
    f'{SETTINGS_PATH}/components/_paths.py',
    f'{SETTINGS_PATH}/components/*.py'
)

PROFILE = 'test'
