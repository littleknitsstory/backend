from settings.components.redis import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/3",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_CLASS_KWARGS": {
                "max_connections": 50,
                "timeout": 20,
                "retry_on_timeout": True,
            },
            "MAX_CONNECTIONS": 1000,
            "PICKLE_VERSION": -1,
        },
    }
}

if REDIS_PASSWORD:
    CACHES["default"]["OPTIONS"]["PASSWORD"] = REDIS_PASSWORD
