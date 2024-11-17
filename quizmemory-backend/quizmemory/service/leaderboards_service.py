import redis
from quizmemory.model.question import Question
class LeaderboardsService:
    def __init__(self,redis_pool):
        self.redis_pool = redis_pool
    
    def calcula_tempo_medio_per_question(self,question_id):
        with redis.Redis(connection_pool=self.redis_pool) as r:
            return int(r.get(f'statistics:{question_id}:total_time'))/int(r.get(f'statistics:{question_id}:total_answers'))
    def ranking_tempo_medio(self,quiz_id):
        with redis.Redis(connection_pool=self.redis_pool) as r:
            questions = r.lrange(f'{quiz_id}:questions',0,-1)
            return (sorted(({question_id:self.calcula_tempo_medio_per_question(question_id) for question_id in questions}).items(),key=lambda x:-x[1]))
    def calcula_alternativas_per_question(self,question_id):
        with redis.Redis(connection_pool=self.redis_pool) as r:
            alternativas=['A','B','C','D']
            total_votos_por_alternativa = {}
            for alternativa in alternativas:
                data = r.get(f'statistics:{question_id}:alternativa:{alternativa}')
                total_votos_por_alternativa[alternativa] = int(data if data else 0)
            return (sorted(total_votos_por_alternativa.items(),key=lambda x:-x[1]))

            
    def ranking_alternativas(self,quiz_id):
        with redis.Redis(connection_pool=self.redis_pool) as r:
            questions = r.lrange(f'{quiz_id}:questions',0,-1)
            return {question_id:self.calcula_alternativas_per_question(question_id) for question_id in questions}

    def ranking_questoes_corretas(self,quiz_id):
        with redis.Redis(connection_pool=self.redis_pool) as r:
            return r.zrevrange(f'leaderboard:{quiz_id}:total_correct_by_question',0,-1,withscores=True)
        
    def ranking_questoes_abstencoes(self,quiz_id):
        with redis.Redis(connection_pool=self.redis_pool) as r:
            return r.zrevrange(f'leaderboard:{quiz_id}:total_invalid_answers',0,-1,withscores=True)
    def ranking_alunos_maior_acerto(self,quiz_id,qnt=-1):
        with redis.Redis(connection_pool=self.redis_pool) as r:
            return r.zrevrange(f'leaderboard:mais_acertos:{quiz_id}',0,qnt,withscores=True)
        # return r.zrevrange(f'leaderboard:mais_acertos:{quiz_id}',0,1000,withscores=True)
    def ranking_mais_rapidos_corretos(self,quiz_id,qnt=-1):
        with redis.Redis(connection_pool=self.redis_pool) as r:
            return r.zrevrange(f'leaderboard:mais_rapidos_corretos_e_acertos:{quiz_id}',0,qnt,withscores=True)
        # return r.zrange(,0,-1,withscores=True)
    def ranking_mais_rapidos(self,quiz_id):
        with redis.Redis(connection_pool=self.redis_pool) as r:
            return r.zrange(f'leaderboard:{quiz_id}:mais_rapido',0,-1,withscores=True)
    def get_leaderboard(self,quiz_num,leaderboard_num):
        match leaderboard_num:
            case 1:
                return self.ranking_alternativas(f'quiz:{quiz_num}')
            case 2:
                return self.ranking_questoes_corretas(f'quiz:{quiz_num}')
            case 3:
                return self.ranking_questoes_abstencoes(f'quiz:{quiz_num}')
            case 4:
                return self.ranking_tempo_medio(f'quiz:{quiz_num}')
            case 5:
                return self.ranking_mais_rapidos_corretos(f'quiz:{quiz_num}',100)
            case 6:
                return self.ranking_alunos_maior_acerto(f'quiz:{quiz_num}',100)
            case 7:
                return self.ranking_mais_rapidos(f'quiz:{quiz_num}')
            case _:
                raise Exception("Numero de leaderboard nao ncontrado")
            
        