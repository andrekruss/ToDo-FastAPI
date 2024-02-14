from pydantic import BaseModel

class CreateTaskDTO(BaseModel):
    board_id: int
    title: str
    description: str | None = None

class TaskDTO(BaseModel):
    id: int | None = None
    user_id: int
    board_id: int 
    title: str
    description: str | None = None
    is_active: bool