from fastapi import APIRouter
import time
from APP.data_models.rest_data_models.request_data_models import RegisterUser, LoginUser, SendMailData
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


@router.post('/sendMail')
def send_mail(send_mail_data: SendMailData):
    log_id = str(int(time.time()))
    service = Service(log_id, 'send_mail_data.sender')
    return service.send_mail(send_mail_data)
