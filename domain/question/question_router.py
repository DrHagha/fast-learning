from fastapi import APIRouter, Depends



from database import SessionLocal, get_db
from sqlalchemy.orm import Session
from models import Question

from domain.question import question_crud


router = APIRouter(
    prefix="/api/question",
)


@router.get("/list")
def question_list(db: Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    return _question_list