import redis
from names_generator import generate_name
from multiprocessing import Pool
import random

MAX_PROCESS = 20
redis_pool = redis.ConnectionPool(max_connections=MAX_PROCESS,host="localhost", port=6379, db=0, decode_responses=True)


def register_and_answer(id):
    # print("Hello")
    with redis.Redis(connection_pool=redis_pool) as r:
        r.hset(f'student:{id}',mapping={
            "nome" : generate_name(style="capital")
        })
        chosen_quiz = random.choices(['1','2'])
        questions_ids = r.lrange(f'quiz:{chosen_quiz[0]}:questions',0,-1)
        # print(f'quiz:{chosen_quiz[0]}:questions')
        # print(questions_ids)
        for question_id in questions_ids:
            chosen_answer = random.choices(['a','b','c','d'])[0]
            time_to_anser = random.randint(1,30)
            if time_to_anser <=20:
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
            r.hset(f'answer:{question_id}:student:{id}',mapping=mapping)
            r.expire(f'answer:{question_id}:student:{id}',30*24*3600) #30 dias
    # r.quit()


if __name__ == '__main__':
    ##### ALUNOS
    print("Iniciando processo")
    N_STUDENTS = 500_000
    # register_and_answer(1)
    with Pool(MAX_PROCESS) as p:
        print("Pool Criada")
        p.map(register_and_answer,range(N_STUDENTS),1)



