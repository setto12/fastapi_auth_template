import hashlib
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str):

    # Pre-hash to avoid bcrypt 72 byte limit
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    return pwd_context.hash(password_hash)


def verify_password(plain_password: str, hashed_password: str):

    password_hash = hashlib.sha256(plain_password.encode()).hexdigest()

    return pwd_context.verify(password_hash, hashed_password)


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt