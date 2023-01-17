from models import Question, Answer
from datetime import datetime
from database import SessionLocal

db = SessionLocal()

q= db.query(Question).get(2)
print(q.id)
q.suject = "생각보다 할만하다"
db.commit()

print(q.subject)