from fastapi import FastAPI
from app.api import auth_routes
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_routes.router)