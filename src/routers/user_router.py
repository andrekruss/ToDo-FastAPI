from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.infra.database.config.db_config import get_db
from src.infra.database.repositories.user_repo import UserRepository
from src.dtos.user_dtos import CreateUserDTO, UserDTO, UserLoginDTO, ResponseUserDTO
from src.utils.hash import hash_password, verify_password
from src.utils.token import generate_jwt_token
from src.utils.auth import get_current_user

router = APIRouter()

@router.post('/users', status_code=status.HTTP_201_CREATED, response_model=ResponseUserDTO)
async def create_user(create_user_dto: CreateUserDTO, db: Session = Depends(get_db)):
    create_user_dto.password = hash_password(create_user_dto.password)
    user = UserRepository(db).create(create_user_dto)
    return ResponseUserDTO(
        email=user.email,
        user_name=user.user_name,
        is_active=user.is_active
    )

@router.post('/token')
async def get_access_token(login_form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_login_dto = UserLoginDTO(
        email=login_form_data.username,
        password=login_form_data.password
    )
    user = UserRepository(db).get_by_email(user_login_dto.email)
    if (not user or not verify_password(user_login_dto.password, user.password)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect user or password.")
    jwt_token = generate_jwt_token({"sub": user.email})
    return {
        'access_token': jwt_token,
        'token_type': 'bearer'
    }

@router.get('/me', status_code=status.HTTP_200_OK, response_model=ResponseUserDTO)
async def protected_route(user: UserDTO = Depends(get_current_user)):
    return ResponseUserDTO(
        email=user.email,
        user_name=user.user_name,
        is_active=user.is_active
    )