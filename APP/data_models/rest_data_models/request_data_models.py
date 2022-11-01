from pydantic import BaseModel


class RegisterUser(BaseModel):
    login: str
    password: str
    email: str
    faculty_id: int


class LoginUser(BaseModel):
    login: str
    password: str
