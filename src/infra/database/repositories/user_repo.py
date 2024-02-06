from src.dtos.user_dtos import CreateUserDTO
from sqlalchemy.orm import Session
from src.infra.database.entities.models import User
from passlib.hash import pbkdf2_sha256

def hash_password(plain_password: str) -> str:
    return pbkdf2_sha256.hash(plain_password)

class UserRepository():

    def __init__(self, db: Session):
        self.db = db

    def create(self, user_dto: CreateUserDTO) -> User:
        user = User(
            user_name = user_dto.user_name,
            email = user_dto.email,
            password = hash_password(user_dto.password)
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
        
