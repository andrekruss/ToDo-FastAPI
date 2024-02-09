from pydantic import BaseModel

class CreateBoardDTO(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True

class BoardDTO(CreateBoardDTO):
    id: int
    is_active: bool