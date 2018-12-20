import os

from backend.core.settings.components.common import ROOT_DIR
import logging
from logging import config

LOGGING_CONFIG = None

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(ROOT_DIR, 'debug.log'),
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        }
    },
}
config.dictConfig(LOGGING)


logger = logging.getLogger(__name__)
logger.info('LKS project is starting...')
