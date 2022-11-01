from pydantic import BaseModel


class Error(BaseModel):
    errorCode:int
    description: str
