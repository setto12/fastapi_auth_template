from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.dependencies.auth_dependencies import get_current_user
from app.db import models

from app.db.database import SessionLocal
from app.schemas.auth_schema import UserCreate, UserLogin
from app.services.auth_service import register_user, authenticate_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    return register_user(
        db,
        user.username,
        user.email,
        user.password
    )


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    token = authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/profile")
def get_profile(current_user: models.User = Depends(get_current_user)):

    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
    }