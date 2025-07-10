# app/schemas/user.py

from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True  # ✅ YOU CAN CUSTOMIZE: Use orm_mode to convert DB to schema

class Token(BaseModel):
    access_token: str
    token_type: str