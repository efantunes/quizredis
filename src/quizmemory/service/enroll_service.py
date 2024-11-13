import redis
class EnrollService:
    def __init__(self,redis_pool):
        self.redis_pool = redis_pool
    def enroll(self,quiz_id,student_id):
        with redis.Redis(connection_pool=self.redis_pool) as r:
            r.lpush(f'participants:{quiz_id}',student_id)