from pydantic import BaseModel

class TaskDTO(BaseModel):
    id: int
    title: str
    description: str
    
    class Config:
        orm_mode = True