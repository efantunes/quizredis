import redis
from names_generator import generate_name
from multiprocessing import Pool
import random
from quizmemory.service.answer_service import AnswerService
from quizmemory.service.enroll_service import EnrollService
from quizmemory.config.redis_config import MAX_PROCESS,MyRedisSingletonPool

anser_service = AnswerService(MyRedisSingletonPool.get_instance())
enroll_service = EnrollService(MyRedisSingletonPool.get_instance())

def register_and_answer_v2(id):
        # print("Hello")
    with redis.Redis(connection_pool=MyRedisSingletonPool.get_instance()) as r:
        r.hset(f'student:{id}',mapping={
            "nome" : generate_name(style="capital")
        })
        
        chosen_quiz = random.choices(['1','2','3','4'])[0]
        enroll_service.enroll(f'quiz:{chosen_quiz}',f'student:{id}')
        questions_ids = r.lrange(f'quiz:{chosen_quiz}:questions',0,-1)
        # print(f'quiz:{chosen_quiz[0]}:questions')
        # print(questions_ids)
        for question_id in questions_ids:
            chosen_answer = random.choices(['A','B','C','D'])[0]
            time_to_anser = random.randint(1,21000)
            anser_service.register_response(question_id,id,chosen_answer,time_to_anser)
            
    # r.quit()


if __name__ == '__main__':
    ##### ALUNOS
    print("Iniciando processo")
    # N_STUDENTS = 1_000_000 #para o teste final
    N_STUDENTS = 200_000 #para desenvlvimento de testes mais rapidos 
    # N_STUDENTS = 50_000 #para desenvlvimento de testes mais rapidos 
    # N_STUDENTS = 1_000 #para desenvlvimento de testes mais rapidos 
    # register_and_answer(1)
    with Pool(MAX_PROCESS) as p:
        print("Pool Criada")
        p.map(register_and_answer_v2,range(N_STUDENTS),1)



