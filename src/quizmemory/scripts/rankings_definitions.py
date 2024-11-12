import redis
from redis.commands.search.field import TextField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from quizmemory.config.redis_config import REDIS_HOST,REDIS_PORT

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)


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