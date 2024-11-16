import redis
from quizmemory.model.question import Question
class QuestionService:
    def __init__(self,redis_pool):
        self.redis_pool = redis_pool
    def create_empty_quiz(self,professor_num,title):
        with redis.Redis(connection_pool=self.redis_pool) as r:
            id_quiz_1 = r.incr('quiz_id_counter')

            r.hset(f'quiz:{id_quiz_1}',mapping={
                "created_by" : f"professor:{professor_num}",
                "title": title
            }) 
            return id_quiz_1
    def create_quiz_with_questions(self,professor_num,title,questions: list[Question]):
        with redis.Redis(connection_pool=self.redis_pool) as r:
            quiz_num = self.create_empty_quiz(professor_num,title)
            qnt_questions = len(questions)
            question_ids = [f'quiz:{quiz_num}:question:{i}' for i in range(qnt_questions)]
            
            r.lpush(f'quiz:{quiz_num}:questions',*question_ids)
            r.lpush(f'quiz:active',f'quiz:{quiz_num}')

            for idx,question in enumerate(questions):
                r.hset(f'quiz:{quiz_num}:question:{idx}',mapping=question.get_question_dict())
                r.set(f'quiz:{quiz_num}:question:{idx}:answer',question.get_answer())
    def gel_all_quizzes(self):
        with redis.Redis(connection_pool=self.redis_pool) as r:
            all_quizzes_ids = r.lrange('quiz:active',0,-1)
            quizzes = []
            for quiz_id in all_quizzes_ids:
                d = r.hgetall(quiz_id)
                d['id'] = quiz_id
                quizzes.append(d)
            return quizzes
    def get_questions(self,quiz_num:int):
        with redis.Redis(connection_pool=self.redis_pool) as r:
            questions = r.lrange(f'quiz:{quiz_num}:questions',0,-1)
            question_infos = []
            for question_id in questions:
                question_info =r.hgetall(question_id)
                question_info['id'] = question_id
                question_infos.append(question_info)
            return question_infos
