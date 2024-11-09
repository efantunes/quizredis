import redis
from redis.commands.search.field import TextField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


#	Tempo médio de resposta por questão
mean_time_schema = [
    TextField("question_id",sortable=True),
    TextField("time",sortable=True)
]
mean_time_idx_def = IndexDefinition(prefix=["answer:"], index_type=IndexType.HASH)
r.ft('ranking_tempo_medio').create_index(
    fields=mean_time_schema,
    definition=mean_time_idx_def
)