LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] [%(levelname)-8s] '
                      '[%(message)s] [%(name)s:%(lineno)s - %(funcName)s()]'
        },
        'simple': {
            'format': '%(asctime)s [%(levelname)s] %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'error_console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'warning_email': {
            'level': 'WARNING',
            # TODO email handler
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'src.apps': {
            'level': 'DEBUG',
            'handlers': ['console', 'error_console'],
            'propagate': False
        },

    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    }
}
