import mysql.connector
from APP.messages.error_msg import ServiceErrorMsg
from APP.data_models.rest_data_models.request_data_models import RegisterUser, LoginUser
from APP.data_models.rest_data_models.response_data_models import Error, LoginUserResponse, GetPostsResponse,\
    GetFiledOfStudyListResponse, GetCourseListResponse, GetFacultyListResponse
from APP.database.mysql_manager import MysqlManager
from APP.utils.yaml_manager import YamlData
from APP.enums.status import PostStatus


class Service:
    def __init__(self, log_id: str, user_name: str):
        self.__log_id = log_id
        self.__user_name = user_name
        self.__yaml_data = YamlData()

    def register_user(self, register_user_data: RegisterUser) -> Error:
        mysql_manager = MysqlManager(self.__log_id, self.__user_name, self.__yaml_data.get_mysql_params())

        try:
            mysql_manager.connect()
        except mysql.connector.Error:
            error = Error(errorCode=ServiceErrorMsg.MYSQL_CONNECTION_ERROR.error_id,
                          description=ServiceErrorMsg.MYSQL_CONNECTION_ERROR.description)
        else:
            try:
                if mysql_manager.check_user_existence_by_login(register_user_data.login):
                    error = Error(errorCode=ServiceErrorMsg.USER_LOGIN_EXISTS.error_id,
                                  description=ServiceErrorMsg.USER_LOGIN_EXISTS.description)
                elif mysql_manager.check_user_existence_by_email(register_user_data.email):
                    error = Error(errorCode=ServiceErrorMsg.USER_EMAIL_EXISTS.error_id,
                                  description=ServiceErrorMsg.USER_EMAIL_EXISTS.description)
                else:
                    mysql_manager.register_user(register_user_data)
                    mysql_manager.commit()
                    mysql_manager.disconnect()
                    error = Error(errorCode=ServiceErrorMsg.EVERYTHING_OK.error_id,
                                  description=ServiceErrorMsg.EVERYTHING_OK.description)
            except mysql.connector.Error:
                error = Error(errorCode=ServiceErrorMsg.REGISTER_USER_ERROR.error_id,
                              description=ServiceErrorMsg.REGISTER_USER_ERROR.description)
        return error

    def login_user(self, login_user_data: LoginUser) -> LoginUserResponse:
        mysql_manager = MysqlManager(self.__log_id, self.__user_name, self.__yaml_data.get_mysql_params())
        user_id = -1
        try:
            mysql_manager.connect()
        except mysql.connector.Error:
            error = Error(errorCode=ServiceErrorMsg.MYSQL_CONNECTION_ERROR.error_id,
                          description=ServiceErrorMsg.MYSQL_CONNECTION_ERROR.description)
        else:
            try:
                data = mysql_manager.login_user(login_user_data)
                if data:
                    error = Error(errorCode=ServiceErrorMsg.EVERYTHING_OK.error_id,
                                  description=ServiceErrorMsg.EVERYTHING_OK.description)
                    user_id = data[0][0]
                    mysql_manager.disconnect()
                else:
                    error = Error(errorCode=ServiceErrorMsg.USER_NOT_EXISTS.error_id,
                                  description=ServiceErrorMsg.USER_NOT_EXISTS.description)
            except mysql.connector.Error:
                error = Error(errorCode=ServiceErrorMsg.LOGIN_USER_ERROR.error_id,
                              description=ServiceErrorMsg.LOGIN_USER_ERROR.description)
        return LoginUserResponse(error=error, user_id=user_id)

    def get_posts(self) -> GetPostsResponse:
        mysql_manager = MysqlManager(self.__log_id, self.__user_name, self.__yaml_data.get_mysql_params())
        data = []
        try:
            mysql_manager.connect()
        except mysql.connector.Error:
            error = Error(errorCode=ServiceErrorMsg.MYSQL_CONNECTION_ERROR.error_id,
                          description=ServiceErrorMsg.MYSQL_CONNECTION_ERROR.description)
        else:
            try:
                data = mysql_manager.get_posts(PostStatus.ACTIVE.get_description,
                                               self.__yaml_data.get_select_posts_limit())
                error = Error(errorCode=ServiceErrorMsg.EVERYTHING_OK.error_id,
                              description=ServiceErrorMsg.EVERYTHING_OK.description)
            except mysql.connector.Error:
                error = Error(errorCode=ServiceErrorMsg.GET_POSTS_ERROR.error_id,
                              description=ServiceErrorMsg.GET_POSTS_ERROR.description)
        return GetPostsResponse(error=error, data=data)

    def get_faculty_list(self) -> GetFacultyListResponse:
        mysql_manager = MysqlManager(self.__log_id, self.__user_name, self.__yaml_data.get_mysql_params())
        data = []
        try:
            mysql_manager.connect()
        except mysql.connector.Error:
            error = Error(errorCode=ServiceErrorMsg.MYSQL_CONNECTION_ERROR.error_id,
                          description=ServiceErrorMsg.MYSQL_CONNECTION_ERROR.description)
        else:
            try:
                data = mysql_manager.get_faculty_list()
                error = Error(errorCode=ServiceErrorMsg.EVERYTHING_OK.error_id,
                              description=ServiceErrorMsg.EVERYTHING_OK.description)
            except mysql.connector.Error:
                error = Error(errorCode=ServiceErrorMsg.GET_FACULTY_ERROR.error_id,
                              description=ServiceErrorMsg.GET_FACULTY_ERROR.description)
        return GetFacultyListResponse(error=error, data=data)

    def get_filed_of_study_list(self) -> GetFiledOfStudyListResponse:
        mysql_manager = MysqlManager(self.__log_id, self.__user_name, self.__yaml_data.get_mysql_params())
        data = []
        try:
            mysql_manager.connect()
        except mysql.connector.Error:
            error = Error(errorCode=ServiceErrorMsg.MYSQL_CONNECTION_ERROR.error_id,
                          description=ServiceErrorMsg.MYSQL_CONNECTION_ERROR.description)
        else:
            try:
                data = mysql_manager.get_field_of_study_list()
                error = Error(errorCode=ServiceErrorMsg.EVERYTHING_OK.error_id,
                              description=ServiceErrorMsg.EVERYTHING_OK.description)
            except mysql.connector.Error:
                error = Error(errorCode=ServiceErrorMsg.GET_FILED_OF_STUDY_ERROR.error_id,
                              description=ServiceErrorMsg.GET_FILED_OF_STUDY_ERROR.description)
        return GetFiledOfStudyListResponse(error=error, data=data)

    def get_course_list(self) -> GetCourseListResponse:
        mysql_manager = MysqlManager(self.__log_id, self.__user_name, self.__yaml_data.get_mysql_params())
        data = []
        try:
            mysql_manager.connect()
        except mysql.connector.Error:
            error = Error(errorCode=ServiceErrorMsg.MYSQL_CONNECTION_ERROR.error_id,
                          description=ServiceErrorMsg.MYSQL_CONNECTION_ERROR.description)
        else:
            try:
                data = mysql_manager.get_course()
                error = Error(errorCode=ServiceErrorMsg.EVERYTHING_OK.error_id,
                              description=ServiceErrorMsg.EVERYTHING_OK.description)
            except mysql.connector.Error:
                error = Error(errorCode=ServiceErrorMsg.GET_COURSE_ERROR.error_id,
                              description=ServiceErrorMsg.GET_COURSE_ERROR.description)
        return GetCourseListResponse(error=error, data=data)
