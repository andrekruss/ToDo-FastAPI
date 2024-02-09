from sqlalchemy.orm import Session

# Entities
from src.infra.database.entities.models import User

# DTOs
from src.dtos.user_dtos import CreateUserDTO, UserDTO

class UserRepository():

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, user_dto: CreateUserDTO) -> UserDTO:
        user = User(
            user_name = user_dto.user_name,
            email = user_dto.email,
            password = user_dto.password
        )
        self.db_session.add(user)
        self.db_session.commit()
        self.db_session.refresh(user)

        return UserDTO(
            user_name = user.user_name,
            email = user.email
        )
    
    def get_by_email(self, email: str):
        user = self.db_session.query(User).filter_by(email=email).first()
        return user
        
        
