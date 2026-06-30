from sqlalchemy.orm import Session
from...core.infrastructure.persistence.user_repository import UserRepository

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_repository(db: Session):
    return UserRepository(db)