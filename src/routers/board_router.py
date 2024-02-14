from fastapi import APIRouter, Depends, status
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

@router.post('/boards', status_code=status.HTTP_201_CREATED)
async def create_board(create_board_dto: CreateBoardDTO, current_user: UserDTO = Depends(get_current_user), db_session: Session = Depends(get_db)):
    user_id = current_user.id
    board = BoardRepository(db_session).create(create_board_dto, user_id)
    return board

@router.get('/boards/{board_id}', status_code=status.HTTP_200_OK)
async def get_board_by_id(board_id: int, current_user: UserDTO = Depends(get_current_user), db_session: Session = Depends(get_db)):
    user_id = current_user.id
    board = BoardRepository(db_session).get(user_id, board_id)
    return board


@router.get('/list-boards', status_code=status.HTTP_200_OK)
async def list_boards(current_user: UserDTO = Depends(get_current_user), db_session: Session = Depends(get_db)):
    user_id = current_user.id
    boards = BoardRepository(db_session).list(user_id)
    return boards