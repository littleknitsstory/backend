"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings

Default environment is `developement`.

To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""

from split_settings.tools import optional, include
from decouple import config

CONFIG_NAME = config('DJANGO_ENV') or 'development'

base_settings = [
    'components/common.py',  # standard django settings
    'components/debug_toolbar.py',  # django debug toolbar
    'components/database.py',  # postgres
    'components/social.py',  # social auth
    'components/webpack.py',  # webpack
    'components/emails.py',  # emails
    'components/logger.py',  # emails

    # Select the right env:
    'environments/%s.py' % CONFIG_NAME,
    # Optionally override some settings:
    optional('environments/local.py'),
]

# Include settings:
include(*base_settings)
