from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

# DB config
from src.infra.database.config.db_config import create_db, get_db

# Repos
from src.infra.database.repositories.user_repo import UserRepository

# Entities
from src.infra.database.entities.user import User

# DTOs
from src.dtos.user_dtos import CreateUserDTO

create_db()

app = FastAPI()

@app.get('/')
async def root():
    return {
        "message": "Root response"
    }

@app.post('/users')
async def create_user(user_dto: CreateUserDTO, db: Session = Depends(get_db)):
    user = UserRepository(db).create(user_dto)
    return user