from decouple import config

REDIS_HOST = config("REDIS_HOST", "redis")
REDIS_PORT = config("REDIS_PORT", "6379")
REDIS_PASSWORD = config("REDIS_PASSWORD", None)

CELERY_CACHE_BACKEND = "default"
CELERY_BROKER_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/2"
