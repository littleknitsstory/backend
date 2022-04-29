from src.settings.components.redis import REDIS_PASSWORD, REDIS_HOST, REDIS_PORT

CELERY_CACHE_BACKEND = "default"
CELERY_BROKER_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/2"
