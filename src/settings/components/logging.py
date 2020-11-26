import sys

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s"
            " %(module)s %(process)d"
            " %(thread)d %(message)s"
        },
        "simple": {"format": "%(levelname)s %(asctime)s %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
        },
    },
    "loggers": {},
    "root": {"handlers": ["console"], "level": "DEBUG"},
}
