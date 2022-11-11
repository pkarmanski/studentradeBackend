import email.errors
import sqlite3
import mysql.connector
from APP.messages.error_msg import ServiceErrorMsg
from APP.data_models.rest_data_models.request_data_models import RegisterUser, LoginUser, SendMailData, ForgotPassword, \
    ChangePassword
from APP.data_models.rest_data_models.response_data_models import Error, LoginUserResponse, GetPostsResponse,\
    GetFiledOfStudyListResponse, GetCourseListResponse, GetFacultyListResponse, ValidateTokenResponse
from APP.database.mysql_manager import MysqlManager
from APP.utils.yaml_manager import YamlData
from APP.enums.status import PostStatus
from APP.database.sqlite_manager import insert_user, update_user, select_user, insert_user_forgot_password, \
    select_forgot_code, delete_forgot_user
from APP.utils.data_manger import generate_token, generate_code
from APP.enums.default_data import DefaultValues
from APP.utils.email_manager import create_mail_data


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
        token = DefaultValues.token_default.default
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
                    try:
                        token = generate_token()
                        insert_user(self.__yaml_data.get_sqlite_db(), self.__log_id, user_id, login_user_data.ip, token)
                    except sqlite3.Error:
                        error = Error(errorCode=ServiceErrorMsg.SQLITE_INSERT_ERROR.error_id,
                                      description=ServiceErrorMsg.SQLITE_INSERT_ERROR.description)
                else:
                    error = Error(errorCode=ServiceErrorMsg.USER_NOT_EXISTS.error_id,
                                  description=ServiceErrorMsg.USER_NOT_EXISTS.description)
            except mysql.connector.Error:
                error = Error(errorCode=ServiceErrorMsg.LOGIN_USER_ERROR.error_id,
                              description=ServiceErrorMsg.LOGIN_USER_ERROR.description)
        return LoginUserResponse(error=error, user_id=token)

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

    def validate_token(self, token: str) -> ValidateTokenResponse:
        try:
            user_data = select_user(self.__yaml_data.get_sqlite_db(), self.__log_id, token)
        except sqlite3.Error:
            error = Error(errorCode=ServiceErrorMsg.SQLITE_SELECT_ERROR.error_id,
                          description=ServiceErrorMsg.SQLITE_SELECT_ERROR.description)
        else:
            try:
                if user_data:
                    token = generate_token()
                    update_user(self.__yaml_data.get_sqlite_db(), self.__log_id, user_data[0]['user_id'], token)
                else:
                    token = DefaultValues.token_default.default
                error = Error(errorCode=ServiceErrorMsg.EVERYTHING_OK.error_id,
                              description=ServiceErrorMsg.EVERYTHING_OK.description)
            except sqlite3.Error:
                error = Error(errorCode=ServiceErrorMsg.SQLITE_UPDATE_ERROR.error_id,
                              description=ServiceErrorMsg.SQLITE_UPDATE_ERROR.description)
        return ValidateTokenResponse(error=error, user_id=token)

    # def send_mail(self, send_mail_data: SendMailData):
    #     try:
    #         create_mail_data(send_mail_data.receiver, send_mail_data.subject, send_mail_data.body)
    #         error = Error(errorCode=ServiceErrorMsg.EVERYTHING_OK.error_id,
    #                       description=ServiceErrorMsg.EVERYTHING_OK.description)
    #     except Exception:
    #         error = Error(errorCode=ServiceErrorMsg.SQLITE_UPDATE_ERROR.error_id,
    #                           description=ServiceErrorMsg.SQLITE_UPDATE_ERROR.description)
    #     return error

    def forgot_password_mail(self, forgot_password_data: ForgotPassword) -> Error:
        mysql_manager = MysqlManager(self.__log_id, self.__user_name, self.__yaml_data.get_mysql_params())

        try:
            mysql_manager.connect()
        except mysql.connector.Error:
            error = Error(errorCode=ServiceErrorMsg.MYSQL_CONNECTION_ERROR.error_id,
                          description=ServiceErrorMsg.MYSQL_CONNECTION_ERROR.description)
        else:
            try:
                if mysql_manager.check_user_existence_by_email(forgot_password_data.email):
                    mysql_manager.disconnect()
                    try:
                        create_mail_data(forgot_password_data.email, forgot_password_data.subject, forgot_password_data.body)
                        error = Error(errorCode=ServiceErrorMsg.EVERYTHING_OK.error_id,
                                      description=ServiceErrorMsg.EVERYTHING_OK.description)

                        try:
                            code = generate_code()
                            insert_user_forgot_password(self.__yaml_data.get_sqlite_db(), self.__log_id, user_email=forgot_password_data.email,
                                                        code=code)
                        except sqlite3.Error:
                            error = Error(errorCode=ServiceErrorMsg.SQLITE_INSERT_ERROR.error_id,
                                          description=ServiceErrorMsg.SQLITE_INSERT_ERROR.description)
                    except email.errors.MessageError:
                        error = Error(errorCode=ServiceErrorMsg.FORGOT_PASSWORD_ERROR.error_id,
                                      description=ServiceErrorMsg.FORGOT_PASSWORD_ERROR.description)
                else:
                    error = Error(errorCode=ServiceErrorMsg.FORGOT_PASSWORD_MAIL_ERROR.error_id,
                                  description=ServiceErrorMsg.FORGOT_PASSWORD_MAIL_ERROR.description)
            except mysql.connector.Error:
                error = Error(errorCode=ServiceErrorMsg.FORGOT_PASSWORD_ERROR.error_id,
                              description=ServiceErrorMsg.FORGOT_PASSWORD_ERROR.description)
        return error

    def change_password(self, change_password_data: ChangePassword) -> Error:
        mysql_manager = MysqlManager(self.__log_id, self.__user_name, self.__yaml_data.get_mysql_params())
        try:
            correct_code = select_forgot_code(self.__yaml_data.get_sqlite_db(), self.__log_id, change_password_data.email)
        except sqlite3.Error:
            error = Error(errorCode=ServiceErrorMsg.SQLITE_SELECT_ERROR.error_id,
                          description=ServiceErrorMsg.SQLITE_SELECT_ERROR.description)
        else:
            try:
                if correct_code:
                    if correct_code != change_password_data.code:
                        error = Error(errorCode=ServiceErrorMsg.CODES_NOT_MATCH_ERROR.error_id,
                                      description=ServiceErrorMsg.CODES_NOT_MATCH_ERROR.description)
                    else:
                        try:
                            mysql_manager.connect()
                        except mysql.connector.Error:
                            error = Error(errorCode=ServiceErrorMsg.MYSQL_CONNECTION_ERROR.error_id,
                                          description=ServiceErrorMsg.MYSQL_CONNECTION_ERROR.description)
                        else:
                            try:
                                mysql_manager.change_password(change_password_data.email, change_password_data.new_password)
                                delete_forgot_user(self.__yaml_data.get_sqlite_db(), change_password_data.email)
                                error = Error(errorCode=ServiceErrorMsg.EVERYTHING_OK.error_id,
                                              description=ServiceErrorMsg.EVERYTHING_OK.description)
                            except mysql.connector.Error:
                                error = Error(errorCode=ServiceErrorMsg.FORGOT_PASSWORD_ERROR.error_id,
                                             description=ServiceErrorMsg.FORGOT_PASSWORD_ERROR.description)
                            except sqlite3.Error:
                                error = Error(errorCode=ServiceErrorMsg.FORGOT_PASSWORD_ERROR.error_id,
                                          description=ServiceErrorMsg.FORGOT_PASSWORD_ERROR.description)
                else:
                    error = Error(errorCode = ServiceErrorMsg.CHANGE_PASSWORD_OUT_TIME_ERROR.error_id,
                                  description=ServiceErrorMsg.CHANGE_PASSWORD_OUT_TIME_ERROR.description)
        return error
