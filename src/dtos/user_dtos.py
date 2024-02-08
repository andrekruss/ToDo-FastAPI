from pydantic import BaseModel

class UserDTO(BaseModel):
    user_name: str
    email: str

class UserLoginDTO(BaseModel):
    email: str
    password: str

class CreateUserDTO(UserDTO):
    password: str

    class Config:
        orm_mode = True



