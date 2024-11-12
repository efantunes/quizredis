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



if __name__ == '__main__':
    NUMBER_OF_TESTS = 500
    
    with redis.Redis(connection_pool=redis_pool) as r1:
        global r
        r=r1

        # 0. avaliação de performance da captura de respostas
        print(timeit.timeit(stmt='answer_service.register_response("quiz:1:question:1","1","b",16)',setup="from __main__ import answer_service",number=NUMBER_OF_TESTS)/NUMBER_OF_TESTS)
        #1. Alternativas mais votadas
        print(ranking_alternativas("quiz:1"))
        print(ranking_alternativas("quiz:2"))
        print(timeit.timeit(stmt='ranking_alternativas("quiz:1")',setup="from __main__ import ranking_alternativas",number=NUMBER_OF_TESTS)/NUMBER_OF_TESTS)
        print(timeit.timeit(stmt='ranking_alternativas("quiz:2")',setup="from __main__ import ranking_alternativas",number=NUMBER_OF_TESTS)/NUMBER_OF_TESTS)
        #2. Questoes mais acertadas
        #3. Questoes com mais abstencoes
        #4. Tempo medio de resposta por questao
        print(ranking_tempo_medio("quiz:1"))
        print(ranking_tempo_medio("quiz:2"))
        print(timeit.timeit(stmt='ranking_tempo_medio("quiz:1")',setup="from __main__ import ranking_tempo_medio",number=NUMBER_OF_TESTS)/NUMBER_OF_TESTS)
        print(timeit.timeit(stmt='ranking_tempo_medio("quiz:2")',setup="from __main__ import ranking_tempo_medio",number=NUMBER_OF_TESTS)/NUMBER_OF_TESTS)
        #5.Alunos com acertos mais rapidos
        #6.Alunos com maior acerto
        #7. Alunos mais rapidos
