from APP.data_models.rest_data_models.request_data_models import RegisterUser


class Service:
    def __init__(self, log_id: str, user_name: str):
        self.__log_id = log_id
        self.__user_name = user_name


    # def register_user(self, register_user_data: RegisterUser):

