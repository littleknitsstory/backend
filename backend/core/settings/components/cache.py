# from decouple import config
#
# REDIS_PASSWORD = config('REDIS_PASSWORD')
#
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': [
#             'redis://{}:{}/1'.format(config('REDIS_HOST'), config('REDIS_PORT'))
#         ],
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#             'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
#             'CONNECTION_POOL_CLASS_KWARGS': {
#                 'max_connections': 50,
#                 'timeout': 20,
#             },
#             'MAX_CONNECTIONS': 1000,
#             'PICKLE_VERSION': -1,
#         },
#     },
# }
#
# # if REDIS_PASSWORD:
# #     CACHES['default']['OPTIONS']['PASSWORD'] = REDIS_PASSWORD
