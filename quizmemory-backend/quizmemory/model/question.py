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