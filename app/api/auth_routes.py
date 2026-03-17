from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

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
def login(user: UserLogin, db: Session = Depends(get_db)):

    token = authenticate_user(
        db,
        user.username,
        user.password
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }