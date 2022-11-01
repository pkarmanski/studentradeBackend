import mysql.connector
from mysql.connector.cursor import MySQLCursor
from APP.data_models.service_data_models.service_data_models import DatabaseParams
from APP.data_models.rest_data_models.request_data_models import RegisterUser, LoginUser
from APP.messages.info_msg import LogInfoMsg
from APP.messages.error_msg import LogErrorMsg
from APP.database.mysql_query import MysqlQuery
import logging
from typing import List

logger = logging.getLogger(__name__)


class MysqlManager:
    def __init__(self, log_id: str, user_name: str,  db_params: DatabaseParams):
        self.__log_id = log_id
        self.__user_name = user_name
        self.__db_params = db_params
        self.__con = mysql.connector.MySQLConnection()
        self.__cursor = MySQLCursor()

    def connect(self):
        try:
            self.__con = mysql.connector.connect(host=self.__db_params.host, port=self.__db_params.port,
                                                 user=self.__db_params.login, password=self.__db_params.password,
                                                 database=self.__db_params.database)
            self.__cursor = self.__con.cursor()
            logger.info(LogInfoMsg.CONNECTED_TO_MYSQL.description.format(self.__log_id, self.__user_name))
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_CONNECTION_ERROR.description.format(self.__log_id, self.__user_name, e))
            raise e

    def disconnect(self):
        self.__cursor.close()
        self.__con.close()
        logger.info(LogInfoMsg.DISCONNECTED_FROM_MYSQL.description.format(self.__log_id, self.__user_name))

    def commit(self):
        self.__con.commit()
        logger.info(LogInfoMsg.MYSQL_COMMIT_OPERATION.description.format(self.__log_id, self.__user_name))

    def check_user_existence_by_login(self, login: str) -> List:
        try:
            check_user_query = MysqlQuery.CHECK_USER_EXISTENCE_BY_LOGIN.query.format(login)
            logger.info(LogInfoMsg.MYSQL_QUERY.description.format(self.__log_id, self.__user_name, check_user_query))
            cursor = self.__cursor
            cursor.execute(check_user_query)
            data = cursor.fetchall()
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_CHECK_USER_BY_LOGIN_ERROR.description.format(self.__log_id,
                                                                                        self.__user_name, e))
            raise e
        return data

    def check_user_existence_by_email(self, email: str) -> List:
        try:
            check_user_query = MysqlQuery.CHECK_USER_EXISTENCE_BY_EMAIL.query.format(email)
            logger.info(LogInfoMsg.MYSQL_QUERY.description.format(self.__log_id, self.__user_name, check_user_query))
            cursor = self.__cursor
            cursor.execute(check_user_query)
            data = cursor.fetchall()
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_CHECK_USER_BY_EMAIL_ERROR.description.format(self.__log_id,
                                                                                        self.__user_name, e))
            raise e
        return data

    def register_user(self, register_user_data: RegisterUser):
        try:
            register_user_query = MysqlQuery.REGISTER_USER.query.format(register_user_data.login,
                                                                        register_user_data.password,
                                                                        register_user_data.email,
                                                                        register_user_data.faculty_id)
            logger.info(LogInfoMsg.MYSQL_QUERY.description.format(self.__log_id, self.__user_name, register_user_data))
            cursor = self.__cursor
            cursor.execute(register_user_query)
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_REGISTER_USER_ERROR.description.format(self.__log_id, self.__user_name, e))
            raise e

    def login_user(self, login_user_data: LoginUser) -> List:
        try:
            login_user_query = MysqlQuery.LOGIN_USER.query.format(login_user_data.login, login_user_data.password)
            logger.info(LogInfoMsg.MYSQL_QUERY.description.format(self.__log_id, self.__user_name, login_user_query))
            cursor = self.__cursor
            cursor.execute(login_user_query)
            data = cursor.fetchall()
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_LOGIN_USER_ERROR.description.format(self.__log_id, self.__user_name, e))
            raise e
        return data
