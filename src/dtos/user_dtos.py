from pydantic import BaseModel

class CreateUserDTO(BaseModel):
    user_name: str
    email: str
    password: str
    is_active: bool = True

    class Config:
        orm_mode = True

