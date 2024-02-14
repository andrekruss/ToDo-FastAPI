from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

# Database
from src.infra.database.config.db_config import get_db
from src.infra.database.repositories.task_repo import TaskRepository

# DTOs
from src.dtos.user_dtos import UserDTO
from src.dtos.task_dtos import CreateTaskDTO

# Utils
from src.utils.auth import get_current_user

router = APIRouter()

@router.post('/tasks', status_code=status.HTTP_201_CREATED)
async def create_task(create_task_dto: CreateTaskDTO, current_user: UserDTO = Depends(get_current_user), db_session: Session = Depends(get_db)):
    user_id = current_user.id
    task = TaskRepository(db_session).create(user_id, create_task_dto)
    return task