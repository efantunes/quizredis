import redis
from redis.commands.search.field import TextField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.aggregation import AggregateRequest, Reducer
from redis.commands.search.reducers import avg

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


#	Tempo médio de resposta por questão

agrupamento = (
    AggregateRequest("*")  # Usa "*" para consultar todos os documentos no índice
    .group_by(
        "@question_id",
        avg("@time")
    )
)
cursor = r.ft('ranking_tempo_medio').aggregate(agrupamento)
for item in  cursor.rows:
    print(item)
