from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from quizmemory.service.answer_service import AnswerService
from quizmemory.service.enroll_service import  EnrollService
from quizmemory.service.question_service import  QuestionService
from quizmemory.config.redis_config import MyRedisSingletonPool
from quizmemory.service.leaderboards_service import LeaderboardsService
import redis
from quizmemory.model.answer_request import AnswerRequest,EnrollRequest

MAX_PROCESS = 20
answer_service = AnswerService(MyRedisSingletonPool.get_instance())
enroll_service = EnrollService(MyRedisSingletonPool.get_instance())
question_service = QuestionService(MyRedisSingletonPool.get_instance())
leaderboard_service = LeaderboardsService(MyRedisSingletonPool.get_instance())

origins = [
    "http://localhost",
    "http://localhost:5000",
    "http://localhost:5001",
    "http://localhost:4200",
    "*",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/quiz/{quiz_num}/question/{question_num}/answer")
def post_response(quiz_num: int,question_num:int, request_body:AnswerRequest):
    answer_service.register_response(
        question_id=f'quiz:{quiz_num}:question:{question_num}',
        student_id=request_body.student_id,
        chosen_answer=request_body.answer,
        time_to_anser=request_body.time
    )
    return {"status": "Sucesso"}

@app.post("/quiz/{quiz_num}/enroll")
def post_enroll(quiz_num: int, request_body:EnrollRequest):
    enroll_service.enroll(
        quiz_id=f'quiz:{quiz_num}',
        student_id=request_body.student_id,
    )
    return {"status": "Sucesso"}

@app.get("/quiz")
def get_all_quizzes():
    return question_service.gel_all_quizzes()

@app.get("/quiz/{quiz_num}/questions")
def get_all_quizzes(quiz_num:int):
    return question_service.get_questions(quiz_num)

@app.get("/quiz/{quiz_num}/leaderboards/{leaderboard_num}")
def get_all_quizzes(quiz_num:int,leaderboard_num:int):
    return leaderboard_service.get_leaderboard(quiz_num,leaderboard_num)
    