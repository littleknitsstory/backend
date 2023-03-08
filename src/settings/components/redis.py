import redis

from decouple import config

REDIS_HOST = config("REDIS_HOST", "redis")
REDIS_PORT = config("REDIS_PORT", "6379")
REDIS_PASSWORD = config("REDIS_PASSWORD", None)


REDIS_CONNECT = redis.StrictRedis(
    host=REDIS_HOST, port=REDIS_PORT, db=3, password=REDIS_PASSWORD
)
