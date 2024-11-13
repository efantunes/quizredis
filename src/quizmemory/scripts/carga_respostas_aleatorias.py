import redis
from names_generator import generate_name
from multiprocessing import Pool
import random
from quizmemory.service.answer_service import AnswerService
from quizmemory.service.enroll_service import EnrollService
from quizmemory.config.redis_config import REDIS_HOST,REDIS_PORT

MAX_PROCESS = 20
redis_pool = redis.ConnectionPool(max_connections=MAX_PROCESS,host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)
anser_service = AnswerService(redis_pool)
enroll_service = EnrollService(redis_pool)

# def register_and_answer(id):
#     # print("Hello")
#     with redis.Redis(connection_pool=redis_pool) as r:
#         r.hset(f'student:{id}',mapping={
#             "nome" : generate_name(style="capital")
#         })
#         chosen_quiz = random.choices(['1','2'])
#         questions_ids = r.lrange(f'quiz:{chosen_quiz[0]}:questions',0,-1)
#         # print(f'quiz:{chosen_quiz[0]}:questions')
#         # print(questions_ids)
#         for question_id in questions_ids:
#             chosen_answer = random.choices(['a','b','c','d'])[0]
#             time_to_anser = random.randint(1,30)
#             if time_to_anser <=20:
#                 mapping={
#                     'answer' : 'invalid',
#                     'time': 'invalid',
#                     "question_id": question_id
#                 }
#             else:
#                 mapping={
#                     'answer' : chosen_answer,
#                     'time': time_to_anser,
#                     "question_id": question_id
#                 }
#             # print(f"Setting: {f'{question_id}:student:{id}'}")
#             r.hset(f'answer:{question_id}:student:{id}',mapping=mapping)
#             r.expire(f'answer:{question_id}:student:{id}',30*24*3600) #30 dias
#     # r.quit()


def register_and_answer_v2(id):
        # print("Hello")
    with redis.Redis(connection_pool=redis_pool) as r:
        r.hset(f'student:{id}',mapping={
            "nome" : generate_name(style="capital")
        })
        
        chosen_quiz = random.choices(['1','2'])[0]
        enroll_service.enroll(f'quiz:{chosen_quiz}',f'student:{id}')
        questions_ids = r.lrange(f'quiz:{chosen_quiz}:questions',0,-1)
        # print(f'quiz:{chosen_quiz[0]}:questions')
        # print(questions_ids)
        for question_id in questions_ids:
            chosen_answer = random.choices(['a','b','c','d'])[0]
            time_to_anser = random.randint(1,30)
            anser_service.register_response(question_id,id,chosen_answer,time_to_anser)
            
    # r.quit()


if __name__ == '__main__':
    ##### ALUNOS
    print("Iniciando processo")
    # N_STUDENTS = 1_000_000 #para o teste final
    # N_STUDENTS = 200_000 #para desenvlvimento de testes mais rapidos 
    N_STUDENTS = 50_000 #para desenvlvimento de testes mais rapidos 
    # register_and_answer(1)
    with Pool(MAX_PROCESS) as p:
        print("Pool Criada")
        p.map(register_and_answer_v2,range(N_STUDENTS),1)



