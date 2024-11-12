from pydantic import BaseModel

class AnswerRequest(BaseModel):
    student_id: str | None = None
    time: int
    answer: str | None = None