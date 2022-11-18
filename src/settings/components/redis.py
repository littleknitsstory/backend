import redis

#from decouple import config

REDIS_HOST = "localhost" #config("REDIS_HOST", "redis")
REDIS_PORT = 6379 #config("REDIS_PORT", "6379")
REDIS_PASSWORD = None #config("REDIS_PASSWORD", None)


REDIS_CONNECT = redis.StrictRedis(
    host=REDIS_HOST, port=REDIS_PORT, db=3, password=REDIS_PASSWORD
)

