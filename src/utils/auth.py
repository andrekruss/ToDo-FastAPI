from fastapi import Depends
from sqlalchemy.orm import Session
from src.infra.database.config.db_config import get_db
from src.infra.database.repositories.user_repo import UserRepository
from src.dtos.user_dtos import UserDTO
from src.utils.token import decode_jwt_token
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme), db_session: Session = Depends(get_db)) -> UserDTO:
    email = decode_jwt_token(token)
    user = UserRepository(db_session).get_by_email(email)
    return UserDTO(
        id=user.id,
        user_name=user.user_name,
        email=email
    )
    
    