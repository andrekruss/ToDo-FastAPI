from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# DTOs
from src.dtos.user_dtos import UserDTO
from src.dtos.board_dtos import CreateBoardDTO

# Database
from src.infra.database.config.db_config import get_db
from src.infra.database.repositories.board_repo import BoardRepository

# Utilities
from src.utils.auth import get_current_user

router = APIRouter()

@router.post('/boards')
async def create_board(create_board_dto: CreateBoardDTO ,current_user: UserDTO = Depends(get_current_user), db_session: Session = Depends(get_db)):
    user_id = current_user.id
    board_dto = BoardRepository(db_session).create(create_board_dto, user_id)
    return board_dto