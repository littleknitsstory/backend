# import sys
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(asctime)s %(message)s'
#         },
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'stream': sys.stdout,
#         },
#         'db_log': {
#             'level': 'DEBUG',
#             'class': 'django_db_logger.db_log_handler.DatabaseLogHandler',
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         'db': {
#             'handlers': ['db_log'],
#             'level': 'DEBUG'
#         },
#     },
#     'root': {
#         'handlers': ['console'],
#         'level': 'DEBUG'
#     },
# }
