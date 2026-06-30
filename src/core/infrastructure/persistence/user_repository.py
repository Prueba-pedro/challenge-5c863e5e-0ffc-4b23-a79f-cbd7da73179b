from sqlalchemy.orm import Session
from..domain.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def update(self, user_id: int, user_update: UserUpdate) -> User:
        user = self.get(user_id)
        if user is None:
            raise Exception("User not found")
        for key, value in user_update.dict(exclude_unset=True).items():
            setattr(user, key, value)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user_id: int) -> None:
        user = self.get(user_id)
        if user is None:
            raise Exception("User not found")
        self.db.delete(user)
        self.db.commit()