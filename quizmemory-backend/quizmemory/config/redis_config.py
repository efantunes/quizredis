import os
import redis

REDIS_HOST = os.environ.get('REDIS_HOST',"localhost") #
REDIS_PORT = os.environ.get('REDIS_PORT',6379) # 

MAX_PROCESS = 20

class MyRedisSingletonPool:
    redis_pool = None
    @staticmethod
    def get_instance():
        if MyRedisSingletonPool.redis_pool:
            return MyRedisSingletonPool.redis_pool
        else:
            MyRedisSingletonPool.redis_pool =redis.ConnectionPool(max_connections=MAX_PROCESS,host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)
            return MyRedisSingletonPool.redis_pool
