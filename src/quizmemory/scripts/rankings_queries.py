import redis
from redis.commands.search.field import TextField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.aggregation import AggregateRequest, Reducer
from redis.commands.search.reducers import avg
import timeit
from quizmemory.service.answer_service import AnswerService
from quizmemory.config.redis_config import REDIS_HOST,REDIS_PORT

MAX_PROCESS = 20
redis_pool = redis.ConnectionPool(max_connections=MAX_PROCESS,host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)
answer_service = AnswerService(redis_pool)
# #	Tempo médio de resposta por questão

# agrupamento = (
#     AggregateRequest("*")  # Usa "*" para consultar todos os documentos no índice
#     .group_by(
#         "@question_id",
#         avg("@time")
#     )
# )
# cursor = r.ft('ranking_tempo_medio').aggregate(agrupamento)
# for item in  cursor.rows:
#     print(item)

def calcula_tempo_medio_per_question(question_id):
    return int(r.get(f'statistics:{question_id}:total_time'))/int(r.get(f'statistics:{question_id}:total_answers'))
def ranking_tempo_medio(quiz_id):
    questions = r.lrange(f'{quiz_id}:questions',0,-1)
    return (sorted(({question_id:calcula_tempo_medio_per_question(question_id) for question_id in questions}).items(),key=lambda x:-x[1]))
def calcula_alternativas_per_question(question_id):
    alternativas=['a','b','c','d']
    total_votos_por_alternativa = {
        alternativa:int(
            r.get(f'statistics:{question_id}:alternativa:{alternativa}')
        ) for alternativa in alternativas
    }
    return (sorted(total_votos_por_alternativa.items(),key=lambda x:-x[1]))

        
def ranking_alternativas(quiz_id):
    questions = r.lrange(f'{quiz_id}:questions',0,-1)
    return {question_id:calcula_alternativas_per_question(question_id) for question_id in questions}

def ranking_questoes_corretas(quiz_id):
    questions = r.lrange(f'{quiz_id}:questions',0,-1)
    acertos_por_questao = {question_id:r.get(f'statistics:{question_id}:total_correct') for question_id in questions}
    return sorted(acertos_por_questao.items(),key = lambda x: -x[1])

# def ranking_alunos_maior_acerto(quiz_id):
#     participants = r.lrange(f"participants:{quiz_id}",0,-1)
#     # print(participants)
#     pontuacao_total_acertos = dict()
#     for participant in participants:
#         acertos = r.get(f'statistics:{quiz_id}:{participant}')
#         if acertos:
#             pontuacao_total_acertos[participant]=acertos
        
#     return sorted(pontuacao_total_acertos.items(), key= lambda x:-int(x[1]))
    # questions = r.lrange(f'{quiz_id}:questions',0,-1)
    # acertos_por_questao = {question_id:r.get(f'statistics:{question_id}:total_correct') for question_id in questions}
    # return sorted(acertos_por_questao.items(),key = lambda x: -x[1])
def ranking_alunos_maior_acerto(quiz_id):
    return r.zrevrange(f'leaderboard:mais_acertos:{quiz_id}',0,-1,withscores=True)
    # return r.zrevrange(f'leaderboard:mais_acertos:{quiz_id}',0,1000,withscores=True)

   
        
     


if __name__ == '__main__':
    NUMBER_OF_TESTS = 50
    
    with redis.Redis(connection_pool=redis_pool) as r1:
        global r
        r=r1
        print ("")
        # 0. Avaliação de performance da captura de respostas
        print ("0. Avaliação de performance da captura de respostas")
        print(timeit.timeit(stmt='answer_service.register_response("quiz:1:question:1","1","b",16)',setup="from __main__ import answer_service",number=NUMBER_OF_TESTS)/NUMBER_OF_TESTS)
        #1. Alternativas mais votadas
        print ("1. Alternativas mais votadas")
        print(ranking_alternativas("quiz:1"))
        print(ranking_alternativas("quiz:2"))
        print(timeit.timeit(stmt='ranking_alternativas("quiz:1")',setup="from __main__ import ranking_alternativas",number=NUMBER_OF_TESTS)/NUMBER_OF_TESTS)
        print(timeit.timeit(stmt='ranking_alternativas("quiz:2")',setup="from __main__ import ranking_alternativas",number=NUMBER_OF_TESTS)/NUMBER_OF_TESTS)
        #2. Questoes mais acertadas
        # print ("2. Questoes mais acertadas")
        # print(ranking_questoes_corretas("quiz:1"))
        # print(ranking_questoes_corretas("quiz:2"))
        # print(timeit.timeit(stmt='ranking_questoes_corretas("quiz:1")',setup="from __main__ import ranking_questoes_corretas",number=NUMBER_OF_TESTS)/NUMBER_OF_TESTS)
        # print(timeit.timeit(stmt='ranking_questoes_corretas("quiz:2")',setup="from __main__ import ranking_questoes_corretas",number=NUMBER_OF_TESTS)/NUMBER_OF_TESTS)
        #3. Questoes com mais abstencoes
        #4. Tempo medio de resposta por questao
        print ("4. Tempo medio de resposta por questao")
        print(ranking_tempo_medio("quiz:1"))
        print(ranking_tempo_medio("quiz:2"))
        print(timeit.timeit(stmt='ranking_tempo_medio("quiz:1")',setup="from __main__ import ranking_tempo_medio",number=NUMBER_OF_TESTS)/NUMBER_OF_TESTS)
        print(timeit.timeit(stmt='ranking_tempo_medio("quiz:2")',setup="from __main__ import ranking_tempo_medio",number=NUMBER_OF_TESTS)/NUMBER_OF_TESTS)
        #5.Alunos com acertos mais rapidos
        #6.Alunos com maior acerto
        print ("6.Alunos com maior acerto")
        print(ranking_alunos_maior_acerto("quiz:1"))
        print(ranking_alunos_maior_acerto("quiz:2"))
        print(timeit.timeit(stmt='ranking_alunos_maior_acerto("quiz:1")',setup="from __main__ import ranking_alunos_maior_acerto",number=NUMBER_OF_TESTS)/NUMBER_OF_TESTS)
        print(timeit.timeit(stmt='ranking_alunos_maior_acerto("quiz:2")',setup="from __main__ import ranking_alunos_maior_acerto",number=NUMBER_OF_TESTS)/NUMBER_OF_TESTS)
        #7. Alunos mais rapidos
