from decouple import config

REDIS_HOST = config('REDIS_HOST')
REDIS_PORT = config('REDIS_PORT')
REDIS_PASSWORD = config('REDIS_PASSWORD')

CACHES = {
	"default": {
		"BACKEND": "django_redis.cache.RedisCache",
		"LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/1",
		"OPTIONS": {
			"CLIENT_CLASS": "django_redis.client.DefaultClient",
			'CONNECTION_POOL_CLASS_KWARGS': {
				'max_connections': 50,
				'timeout': 20,
				'retry_on_timeout': True
			},
			'MAX_CONNECTIONS': 1000,
			'PICKLE_VERSION': -1,
		}
	}
}
if REDIS_PASSWORD:
	CACHES['default']['OPTIONS']['PASSWORD'] = REDIS_PASSWORD
