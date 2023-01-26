from pydantic import BaseModel


class AnswerCreate(BaseModel):
    content : str
    
    @validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈값은 허용되지 않습니다')
        return v