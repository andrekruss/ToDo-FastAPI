from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

# DB config
from src.infra.database.config.db_config import create_db, get_db

# Repos
from src.infra.database.repositories.user_repo import UserRepository

# Entities
from src.infra.database.entities.user import User

# DTOs
from src.dtos.user_dtos import CreateUserDTO, UserDTO

create_db()

app = FastAPI()

@app.post('/users', status_code=status.HTTP_201_CREATED, response_model=UserDTO)
async def create_user(user_dto: CreateUserDTO, db: Session = Depends(get_db)):
    user = UserRepository(db).create(user_dto)
    return UserDTO(
        user_name=user.user_name,
        email=user.email,
        is_active=user.is_active
    )