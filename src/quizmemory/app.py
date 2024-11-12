from typing import Union

from fastapi import FastAPI
from quizmemory.service.answer_service import AnswerService
from quizmemory.config.redis_config import REDIS_HOST,REDIS_PORT
import redis
from quizmemory.model.answer_request import AnswerRequest

MAX_PROCESS = 20
redis_pool = redis.ConnectionPool(max_connections=MAX_PROCESS,host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)
answer_service = AnswerService(redis_pool)

app = FastAPI()


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