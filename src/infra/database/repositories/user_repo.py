from sqlalchemy.orm import Session
from src.dtos.user_dtos import CreateUserDTO
from src.infra.database.entities.user import User

class UserRepository():

    def __init__(self, db: Session):
        self.db = db

    def create(self, user_dto: CreateUserDTO) -> User:
        user = User(
            user_name = user_dto.user_name,
            email = user_dto.email,
            password = user_dto.password,
            is_active = user_dto.is_active
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
        
