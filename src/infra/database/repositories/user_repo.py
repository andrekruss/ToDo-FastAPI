from src.dtos.user_dtos import CreateUserDTO, UserLoginDTO
from sqlalchemy.orm import Session
from src.infra.database.entities.models import User

class UserRepository():

    def __init__(self, db: Session):
        self.db = db

    def create(self, user_dto: CreateUserDTO) -> User:
        user = User(
            user_name = user_dto.user_name,
            email = user_dto.email,
            password = user_dto.password
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get(self, user_login: UserLoginDTO):
        user = self.db.query(User).filter_by(email=user_login.email).first()
        return user
        
        
