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


class SendMailData(BaseModel):
    # sender: str
    receiver: str
    subject: str
    body: str


class ForgotPassword(BaseModel):
    email: str
    subject: str
    body: str


class ChangePassword(BaseModel):
    email: str
    code: str
    new_password: str
