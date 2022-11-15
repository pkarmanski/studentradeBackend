from pydantic import BaseModel
from typing import List


class Error(BaseModel):
    errorCode: int
    description: str


class LoginUserResponse(BaseModel):
    user_id: str
    error: Error
    login: str


class GetPostsResponse(BaseModel):
    data: List
    error: Error


class GetFacultyListResponse(BaseModel):
    data: List
    error: Error


class GetCourseListResponse(BaseModel):
    data: List
    error: Error


class GetFiledOfStudyListResponse(BaseModel):
    data: List
    error: Error


class ValidateTokenResponse(BaseModel):
    user_id: str
    login: str
    error: Error
