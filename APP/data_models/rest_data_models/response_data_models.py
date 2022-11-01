from pydantic import BaseModel


class Error(BaseModel):
    errorCode: int
    description: str


class LoginUserResponse(BaseModel):
    user_id: int
    error: Error
