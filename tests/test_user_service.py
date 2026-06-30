from unittest.mock import MagicMock
from...core.application.user_service import UserService
from...core.domain.user import UserCreate, UserUpdate
from...core.infrastructure.persistence.user_repository import UserRepository

def test_create_user():
    user_repository = MagicMock(UserRepository)
    user_service = UserService(user_repository)
    user_create = UserCreate(name="John Doe", email="john@example.com", role="admin", password="password")
    user = user_service.create_user(user_create)
    assert user.name == user_create.name
    assert user.email == user_create.email
    assert user.role == user_create.role

def test_get_user():
    user_repository = MagicMock(UserRepository)
    user_repository.get.return_value = UserCreate(id=1, name="John Doe", email="john@example.com", role="admin", password="password")
    user_service = UserService(user_repository)
    user = user_service.get_user(1)
    assert user.name == "John Doe"
    assert user.email == "john@example.com"
    assert user.role == "admin"

def test_update_user():
    user_repository = MagicMock(UserRepository)
    user_repository.get.return_value = UserCreate(id=1, name="John Doe", email="john@example.com", role="admin", password="password")
    user_service = UserService(user_repository)
    user_update = UserUpdate(name="Jane Doe", email="jane@example.com")
    user = user_service.update_user(1, user_update)
    assert user.name == "Jane Doe"
    assert user.email == "jane@example.com"

def test_delete_user():
    user_repository = MagicMock(UserRepository)
    user_repository.get.return_value = UserCreate(id=1, name="John Doe", email="john@example.com", role="admin", password="password")
    user_service = UserService(user_repository)
    user_service.delete_user(1)
    user_repository.delete.assert_called_once_with(1)