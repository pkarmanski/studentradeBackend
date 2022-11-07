from pydantic import BaseModel
from typing import Optional


class RegisterUser(BaseModel):
    login: str
    password: str
    email: str
    facultyId: int
    ip: Optional[str] = ''


class LoginUser(BaseModel):
    login: str
    password: str
    ip: Optional[str] = ''
