from fastapi import APIRouter, Depends



from database import SessionLocal, get_db
from sqlalchemy.orm import Session
from models import Question

from domain.question import question_schema, question_crud


router = APIRouter(
    prefix="/api/question",
)


@router.get("/list")
def question_list(db: Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    return _question_list

@router.get("/detail/{question_id}")
def question_detail(question_id: int, db: Session = Depends(get_db)):
    
    question = question_crud.get_question(db, question_id=question_id)
    return question