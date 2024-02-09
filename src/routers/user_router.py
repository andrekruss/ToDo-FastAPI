from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.infra.database.config.db_config import get_db
from src.infra.database.repositories.user_repo import UserRepository
from src.dtos.user_dtos import CreateUserDTO, UserDTO, UserLoginDTO
from src.utils.hash import hash_password, verify_password
from src.utils.token import generate_jwt_token, decode_jwt_token
from src.utils.auth import oauth2_scheme

router = APIRouter()

@router.post('/users', status_code=status.HTTP_201_CREATED, response_model=UserDTO)
async def create_user(user_dto: CreateUserDTO, db: Session = Depends(get_db)):
    user_dto.password = hash_password(user_dto.password)
    user = UserRepository(db).create(user_dto)
    return UserDTO(
        user_name=user.user_name,
        email=user.email,
        is_active=user.is_active
    )

@router.post('/login', status_code=status.HTTP_200_OK)
async def login(user_login_dto: UserLoginDTO, db: Session = Depends(get_db)):
    user = UserRepository(db).get(user_login_dto.email)
    if (not user or not verify_password(user_login_dto.password, user.password)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect user or password.")
    jwt_token = generate_jwt_token(user.id)
    return {
        'token': jwt_token
    }

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

@router.get('/me')
async def protected_route(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    email = decode_jwt_token(token)
    user = UserRepository(db).get_by_email(email)
    return user
