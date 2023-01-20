from fastapi import APIRouter, Depends

from database import get_db
from domain.question import questions_schema, question_crud
from sqlalchemy.orm import Session

router = APIRouter(
    prefix = "/api/question",
)

@router.get("/list", response_model = list[questions_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    return _question_list