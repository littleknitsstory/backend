import os
from django.conf import settings

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'builds/',
        'CACHE': not settings.DEBUG,
        'POLL_INTERVAL': 0.1,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}

WEBPACK_LOADER.update({
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'builds/',  # must end with slash
        'STATS_FILE': os.path.join(settings.ROOT_DIR, './static/webpack.scss.json'),
    }
})
