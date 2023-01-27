import datetime
from domain.answer import answer_schema
from pydantic import BaseModel

class Question(BaseModel):
    id : int
    subject : str
    content : str
    create_date : datetime.datetime
    answers: list[answer_schema.Answer] = []
    
    class Config:
        orm_mode = True