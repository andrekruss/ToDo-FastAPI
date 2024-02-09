from sqlalchemy.orm import Session

# Entities
from src.infra.database.entities.models import Board

# DTOs
from src.dtos.board_dtos import CreateBoardDTO, BoardDTO

class BoardRepository():

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create(self, createBoardDTO: CreateBoardDTO, user_id: int) -> BoardDTO:
        board = Board(
            user_id=user_id,
            title=createBoardDTO.title,
            description=createBoardDTO.description,
            is_active=True
        )
        self.db_session.add(board)
        self.db_session.commit()
        self.db_session.refresh(board)

        return BoardDTO(
            id = board.id,
            title = board.title,
            description = board.description,
            is_active = board.is_active
        )