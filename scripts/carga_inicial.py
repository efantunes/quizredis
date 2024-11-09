import redis

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)



##### PROFESSORES
id_dumbledore = r.incr('professor_id_counter')
r.hset(f'professor:{id_dumbledore}',mapping={
    "nome" : "Dumbledore"
})
id_snape = r.incr('professor_id_counter')
r.hset(f'professor:{id_snape}',mapping={
    "nome" : "Snape"
})


##### Quizzes

id_quiz_1 = r.incr('quiz_id_counter')
r.hset(f'quiz:{id_quiz_1}',mapping={
    "created_by" : f"professor:{id_snape}",
    "title": "O melhor Quiz do Universo"
})

id_quiz_2 = r.incr('quiz_id_counter')
r.hset(f'quiz:{id_quiz_2}',mapping={
    "created_by" : f"professor:{id_snape}",
    "title": "O segundo melhor Quiz do Universo"
})


######### Perguntas

class Question:
    def __init__(self,question,a,b,c,d,answer):
        self.question = question
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.answer = answer
    def get_question_dict(self):
        return {
            "question" : self.question, 
            "A": self.a, 
            "B": self.b, 
            "C": self.c, 
            "D": self.d 
        }
    def get_answer(self):
        return self.answer


############# Perguntas
### Quiz1
id_quiz_1_question_1=f'quiz:{id_quiz_1}:question:1'
id_quiz_1_question_2=f'quiz:{id_quiz_1}:question:2'
r.lpush(f'quiz:{id_quiz_1}:questions',id_quiz_1_question_1,id_quiz_1_question_2)

q1q1=Question(
    "Qual é o país com a maior população do mundo?",
    "Estados Unidos", "Rússia", "Índia", "China",
    "d"
)
q1q2=Question(
    "Qual desses planetas é conhecido como o 'Planeta Vermelho'?",
    "Vênus", "Marte", "Júpiter", "Saturno",
    "b"
)
r.hset(f'quiz:{id_quiz_1}:question:1',mapping=q1q1.get_question_dict())
r.set(f'quiz:{id_quiz_1}:question:1:answer',q1q1.get_answer())
r.hset(f'quiz:{id_quiz_1}:question:2',mapping=q1q2.get_question_dict())
r.set(f'quiz:{id_quiz_1}:question:2:answer',q1q2.get_answer())

### Quiz2
id_quiz_2_question_1=f'quiz:{id_quiz_2}:question:1'
id_quiz_2_question_2=f'quiz:{id_quiz_2}:question:2'
r.lpush(f'quiz:{id_quiz_2}:questions',id_quiz_2_question_1,id_quiz_2_question_2)

q2q1=Question(
    "Qual é o nome do oceano que fica na costa leste do Brasil?",
    "Oceano Atlântico", "Oceano Pacífico", "Oceano Índico", "Oceano Ártico",
    "a"
)
q2q2=Question(
    "Qual desses animais é considerado o maior mamífero do mundo?",
    "Elefante", "Baleia-azul", "Rinoceronte", "Urso-polar",
    "b"
)


r.hset(f'quiz:{id_quiz_2}:question:1',mapping=q2q1.get_question_dict())
r.set(f'quiz:{id_quiz_2}:question:1:answer',q2q1.get_answer())
r.hset(f'quiz:{id_quiz_2}:question:2',mapping=q2q2.get_question_dict())
r.set(f'quiz:{id_quiz_2}:question:2:answer',q2q2.get_answer())




