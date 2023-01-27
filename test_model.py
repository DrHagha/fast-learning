from models import Question, Answer
from datetime import datetime
from database import SessionLocal

q = Answer(content = "사랑의 모시깽이", question_id = 1, create_date=datetime.now())

db = SessionLocal()
db.add(q)
db.commit()
