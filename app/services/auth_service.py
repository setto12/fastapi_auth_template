from sqlalchemy.orm import Session

from app.db import models
from app.core.security import hash_password, verify_password, create_access_token


def register_user(db: Session, username: str, email: str, password: str):

    hashed_pw = hash_password(password)

    user = models.User(
        username=username,
        email=email,
        hashed_password=hashed_pw
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(db: Session, username: str, password: str):

    user = db.query(models.User).filter(
        models.User.username == username
    ).first()

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    token = create_access_token({"sub": user.username})

    return token