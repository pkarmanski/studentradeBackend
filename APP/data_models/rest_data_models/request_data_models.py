from pydantic import BaseModel
from typing import Optional, Union


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


class UploadPostData(BaseModel):
    userId: str
    content: str
    image: Optional[Union[str, bytes]] = None
    fileName: Optional[str] = None


class ActivateUserData(BaseModel):
    token: str
    code: str


class UploadCommentBody(BaseModel):
    userId: str
    content: str
    postId: int


class UploadProductData(BaseModel):
    userId: str
    title: str
    content: str
    image: Optional[Union[str, bytes]] = None
    fileName: Optional[str] = None
    fieldOfStudy: int
    productType: int
    price: int
    year: float


class FilterProductsData(BaseModel):
    priceMin: str
    priceMax: str
    fieldOfStudyId: int
    uploadDate: str
    yearOfStudy: str
    title: str
    productType: int
