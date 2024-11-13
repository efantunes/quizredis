import redis
class AnswerService:
    def __init__(self,redis_pool):
        self.redis_pool = redis_pool
    def register_response(self,question_id,student_id,chosen_answer,time_to_anser):
        with redis.Redis(connection_pool=self.redis_pool) as r:
            if time_to_anser >20:
                mapping={
                    'answer' : 'invalid',
                    'time': 'invalid',
                    "question_id": question_id
                }
            else:
                mapping={
                    'answer' : chosen_answer,
                    'time': time_to_anser,
                    "question_id": question_id
                }
            # print(f"Setting: {f'{question_id}:student:{id}'}")
            EXPIRATION_TIME = 30*24*3600
            r.hset(f'answer:{question_id}:student:{student_id}',mapping=mapping)
            r.expire(f'answer:{question_id}:student:{student_id}',EXPIRATION_TIME) #30 dias
            
            ## RANKINGS ##

            r.incr(f'statistics:{question_id}:total_time',str(time_to_anser)) 
            r.expire(f'statistics:{question_id}:total_time',EXPIRATION_TIME) #30 dias
            r.incr(f'statistics:{question_id}:total_answers') 
            r.expire(f'statistics:{question_id}:total_answers',EXPIRATION_TIME) #30 dias

            r.incr(f'statistics:{question_id}:alternativa:{chosen_answer}') 
            r.expire(f'statistics:{question_id}:alternativa:{chosen_answer}',EXPIRATION_TIME) #30 dias

            quiz_num = question_id.split(":")[1]
            quiz_id = f"quiz:{quiz_num}"
            correct_answer = r.get(f'{question_id}:answer')
            if correct_answer == chosen_answer:
                r.incr(f'statistics:{question_id}:total_correct') 
                r.expire(f'statistics:{question_id}:total_correct',EXPIRATION_TIME) #30 dias
                r.zincrby(f'leaderboard:mais_acertos:{quiz_id}',1,f'student:{student_id}') 
                r.expire(f'leaderboard:mais_acertos:{quiz_id}',EXPIRATION_TIME) #30 dias