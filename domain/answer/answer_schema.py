from pydantic import BaseModel
from datetime import datetime


class AnswerCreate(BaseModel):
    content : str
    
    @validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈값은 허용되지 않습니다')
        return v
    
class Answer(BaseModel):
    id : int
    content : str
    create_date = datetime
    
    class Config:
        orm_mode = True