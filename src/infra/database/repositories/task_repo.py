from typing import List
from sqlalchemy.orm import Session

# Entities
from src.infra.database.entities.models import Task

# DTOs
from src.dtos.task_dtos import CreateTaskDTO, TaskDTO

class TaskRepository():

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create(self, user_id: int, create_task_dto: CreateTaskDTO) -> TaskDTO:
        task = Task(
            user_id = user_id,
            board_id = create_task_dto.board_id,
            title = create_task_dto.title,
            description = create_task_dto.description
        )

        self.db_session.add(task)
        self.db_session.commit()
        self.db_session.refresh(task)

        return TaskDTO(
            id = task.id,
            user_id = task.user_id,
            board_id = task.board_id,
            title = task.title,
            description = task.description,
            is_active = task.is_active
        )
    
    def get(self, user_id: int, board_id: int, task_id: int) -> TaskDTO | None:
        task = self.db_session.query(Task).filter_by(
            user_id = user_id,
            board_id = board_id,
            id = task_id
        ).first()

        if task:
            return TaskDTO(
                id = task.id,
                user_id = task.user_id,
                board_id = task.board_id,
                title = task.title,
                description = task.description,
                is_active = task.is_active
            )
        return None
    
    def delete(self, user_id: int, board_id: int, task_id: int) -> TaskDTO | None:
        task = self.db_session.query(Task).filter_by(
            user_id = user_id,
            board_id = board_id,
            id = task_id
        ).first()

        if task:
            task_dto = TaskDTO(
                id = task.id,
                user_id = task.user_id,
                board_id = task.board_id,
                title = task.title,
                description = task.description,
                is_active = task.is_active
            )
            self.db_session.delete(task)
            self.db_session.commit()
            return task_dto

        return None
    
    def list(self, user_id: int, board_id: int) -> List[TaskDTO]:
        tasks = self.db_session.query(Task).filter_by(
            user_id = user_id,
            board_id = board_id
        ).all()
        tasks_dtos = [ ]
        for task in tasks:
            task_dto = TaskDTO(
                id = task.id,
                user_id = task.user_id,
                board_id = task.board_id,
                title = task.title,
                description = task.description,
                is_active = task.is_active
            )
            tasks_dtos.append(task_dto)

        return tasks_dtos