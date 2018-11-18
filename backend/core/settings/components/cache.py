
REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
REDIS_PASSWORD = ''

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': [
            '{}:{}'.format(REDIS_HOST, REDIS_PORT)
        ],
        'OPTIONS': {
            'DB': 1,
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
                'timeout': 20,
            },
            'MAX_CONNECTIONS': 1000,
            'PICKLE_VERSION': -1,
        },
    },
}

if REDIS_PASSWORD:
    CACHES['default']['OPTIONS']['PASSWORD'] = REDIS_PASSWORD
