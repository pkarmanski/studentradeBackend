from fastapi import APIRouter
import time
from APP.data_models.rest_data_models.request_data_models import RegisterUser
from APP.service.studentrade_service import Service


router = APIRouter(prefix='/studentrade/v1')


@router.put('/registerUser')
def register_user(register_user_data: RegisterUser):
    log_id = str(int(time.time()))
    service = Service(log_id, register_user_data.login)
    return


