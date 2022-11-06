from pydantic import BaseModel


class RegisterUser(BaseModel):
    login: str
    password: str
    email: str
    facultyId: int


class LoginUser(BaseModel):
    login: str
    password: str
