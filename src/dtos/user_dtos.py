from pydantic import BaseModel

class CreateUserDTO(BaseModel):
    user_name: str
    email: str
    password:str

class UserLoginDTO(BaseModel):
    email: str
    password: str

class ResponseUserDTO(BaseModel):
    user_name: str
    email: str
    is_active: bool

class UserDTO(BaseModel):
    id: int 
    user_name: str 
    email: str
    password: str | None = None
    is_active: bool 
