import logging

from fastapi import APIRouter
import time
from APP.data_models.rest_data_models.request_data_models import RegisterUser, LoginUser, SendMailData, \
    ForgotPassword, ChangePassword, UploadPostData, ActivateUserData
from APP.service.studentrade_service import Service


router = APIRouter(prefix='/studentrade/v1')


@router.put('/registerUser')
def register_user(register_user_data: RegisterUser):
    log_id = str(int(time.time()))
    service = Service(log_id, register_user_data.login)
    return service.register_user(register_user_data)


@router.post('/loginUser')
def login_user(login_user_data: LoginUser):
    log_id = str(int(time.time()))
    service = Service(log_id, login_user_data.login)
    return service.login_user(login_user_data)


@router.get('/getPosts')
def get_post():
    log_id = str(int(time.time()))
    service = Service(log_id, '')
    logging.critical(service.get_posts().json())
    return service.get_posts()


@router.get('/getFacultyList')
def get_faculty_list():
    log_id = str(int(time.time()))
    service = Service(log_id, '')
    return service.get_faculty_list()


@router.get('/getFieldOfStudyList')
def get_faculty_list():
    log_id = str(int(time.time()))
    service = Service(log_id, '')
    return service.get_filed_of_study_list()


@router.get('/getCourseList')
def get_faculty_list():
    log_id = str(int(time.time()))
    service = Service(log_id, '')
    return service.get_course_list()


@router.get('/validateToken/{token}')
def validate_token(token: str):
    log_id = str(int(time.time()))
    service = Service(log_id, token)
    return service.validate_token(token)


@router.post('/forgotPassword')
def forgot_password(forgot_password_data: ForgotPassword):
    log_id = str(int(time.time()))
    service = Service(log_id, forgot_password_data.email)
    return service.forgot_password_mail(forgot_password_data)


@router.put('/changePassword')
def forgot_password(change_password_data: ChangePassword):
    log_id = str(int(time.time()))
    service = Service(log_id, change_password_data.email)
    return service.change_password(change_password_data)


@router.put('/uploadPost')
def make_post(upload_post_data: UploadPostData):
    log_id = str(int(time.time()))
    service = Service(log_id, upload_post_data.userId)
    return service.upload_post(upload_post_data)


@router.put('/activateUser')
def activate_user(activate_user_data: ActivateUserData):
    log_id = str(int(time.time()))
    service = Service(log_id, activate_user_data.token)
    return service.activate_user(activate_user_data.token, activate_user_data.code)

