from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

# Database
from src.infra.database.config.db_config import get_db
from src.infra.database.repositories.task_repo import TaskRepository

# DTOs
from src.dtos.user_dtos import UserDTO
from src.dtos.task_dtos import CreateTaskDTO, TaskDTO

# Utils
from src.utils.auth import get_current_user

router = APIRouter()

@router.post('/tasks', status_code=status.HTTP_201_CREATED, response_model=TaskDTO)
async def create_task(create_task_dto: CreateTaskDTO, current_user: UserDTO = Depends(get_current_user), db_session: Session = Depends(get_db)):
    user_id = current_user.id
    task = TaskRepository(db_session).create(user_id, create_task_dto)
    return task

@router.get('/tasks/{board_id}/{task_id}', status_code=status.HTTP_200_OK, response_model=TaskDTO)
async def get_task_by_id(board_id: int, task_id: int, current_user: UserDTO = Depends(get_current_user), db_session: Session = Depends(get_db)):
    user_id = current_user.id
    task = TaskRepository(db_session).get(
        user_id = user_id,
        board_id = board_id,
        task_id = task_id
    )
    return task

@router.get('/list-tasks/{board_id}', status_code=status.HTTP_200_OK, response_model=List[TaskDTO])
async def list_tasks(board_id: int, current_user: UserDTO = Depends(get_current_user), db_session: Session = Depends(get_db)):
    user_id = current_user.id
    tasks = TaskRepository(db_session).list(
        user_id = user_id,
        board_id = board_id
    )
    return tasks

@router.delete('/tasks/{board_id}/{task_id}', status_code=status.HTTP_200_OK, response_model=TaskDTO)
async def delete_task_by_id(board_id: int, task_id: int, current_user: UserDTO = Depends(get_current_user), db_session: Session = Depends(get_db)):
    user_id = current_user.id
    task = TaskRepository(db_session).delete(
        user_id=user_id,
        board_id=board_id,
        task_id=task_id
    )
    return task