from pydantic import (
    BaseModel,
    EmailStr
)

class UserBase(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    class Config:
        orm_mode = True
