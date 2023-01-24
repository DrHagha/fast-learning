from models import Question
from sqlalchemy.orm import Session

def get_question_list(db: Session):
    print(db)
    question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return question_list
