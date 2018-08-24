"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings

Default environment is `developement`.

To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""
import environ

from split_settings.tools import optional, include

ROOT_DIR = environ.Path(__file__) - 3  # (backend/core/settings/__init__.py - 3 = backend/)
env = environ.Env()
env_file = str(ROOT_DIR.path('../.env'))
print(env_file)
env.read_env(env_file)
print('hello', env.read_env(env_file))

# CUSTOM_ENV = environ.Env()
# CONFIG_NAME = environ.Env.ENVIRON.get('DJANGO_ENV') or 'development'

base_settings = [
    'components/common.py',  # standard django settings
    'components/debug_toolbar.py',  # django debug toolbar
    # 'components/database.py',  # postgres

    # Select the right env:
    # 'environments/%s.py' % CONFIG_NAME,
    # Optionally override some settings:
    # optional('environments/local.py'),
]

# Include settings:
include(*base_settings)
