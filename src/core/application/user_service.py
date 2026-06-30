from..domain.user import User, UserCreate, UserUpdate
from..infrastructure.persistence.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_create: UserCreate) -> User:
        user = User(**user_create.dict())
        return self.user_repository.create(user)

    def get_user(self, user_id: int) -> User:
        return self.user_repository.get(user_id)

    def update_user(self, user_id: int, user_update: UserUpdate) -> User:
        return self.user_repository.update(user_id, user_update)

    def delete_user(self, user_id: int) -> None:
        self.user_repository.delete(user_id)