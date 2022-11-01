from pydantic import BaseModel


class RegisterUser(BaseModel):
    login: str
    password: str
    email: str
    faculty_id: int
