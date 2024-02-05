from pydantic import BaseModel

class BoardDTO(BaseModel):
    id: int
    title: str
    description: str
    is_active: bool

    class Config:
        orm_mode = True