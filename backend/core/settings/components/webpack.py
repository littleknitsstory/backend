import os
from django.conf import settings

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'builds/',
        'STATS_FILE': os.path.join(settings.ROOT_DIR, './static/webpack.scss.json'),
    }
}
