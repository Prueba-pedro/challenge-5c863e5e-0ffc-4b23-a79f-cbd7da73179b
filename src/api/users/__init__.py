from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from...core.application.user_service import UserService
from...core.domain.user import UserCreate, UserUpdate
from...core.infrastructure.security.jwt_utils import authenticate_user

router = APIRouter()

@router.post("/users/", response_model=UserCreate)
def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    return user_service.create_user(user_create)

@router.get("/users/{user_id}", response_model=UserCreate)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=UserCreate)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    return user_service.update_user(user_id, user_update)

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    user_service.delete_user(user_id)
    return {"detail": "User deleted"}