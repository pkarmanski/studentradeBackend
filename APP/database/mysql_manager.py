import mysql.connector
from mysql.connector.cursor import MySQLCursor
from APP.data_models.service_data_models.service_data_models import DatabaseParams
from APP.data_models.rest_data_models.request_data_models import RegisterUser, LoginUser, UploadProductData,\
    FilterProductsData
from APP.messages.info_msg import LogInfoMsg
from APP.messages.error_msg import LogErrorMsg
from APP.database.mysql_query import MysqlQuery
from APP.utils.data_manger import get_current_date, generate_title_filter
from APP.enums.status import UserStatus, PostStatus, ProductStatus

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
                                                                        register_user_data.facultyId,
                                                                        UserStatus.INACTIVE.get_description)
            logger.info(LogInfoMsg.MYSQL_QUERY.description.format(self.__log_id, self.__user_name, register_user_query))
            cursor = self.__cursor
            cursor.execute(register_user_query)
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_REGISTER_USER_ERROR.description.format(self.__log_id, self.__user_name, e))
            raise e

    def login_user(self, login_user_data: LoginUser) -> List:
        try:
            login_user_query = MysqlQuery.LOGIN_USER.query.format(login_user_data.login, login_user_data.password,
                                                                  UserStatus.ACTIVE.get_description)
            logger.info(LogInfoMsg.MYSQL_QUERY.description.format(self.__log_id, self.__user_name, login_user_query))
            cursor = self.__cursor
            cursor.execute(login_user_query)
            data = cursor.fetchall()
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_LOGIN_USER_ERROR.description.format(self.__log_id, self.__user_name, e))
            raise e
        return data

    def get_user_id(self, login: str, password: str, email: str) -> List:
        try:
            get_user_id_query = MysqlQuery.GET_USER_ID.query.format(login, password, email)
            logger.info(LogInfoMsg.MYSQL_QUERY.description.format(self.__log_id, self.__user_name, get_user_id_query))
            cursor = self.__cursor
            cursor.execute(get_user_id_query)
            columns = [item[0] for item in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_LOGIN_USER_ERROR.description.format(self.__log_id, self.__user_name, e))
            raise e
        return data

    def get_posts(self, status: str, post_select_limit: int) -> List:
        try:
            get_post_query = MysqlQuery.GET_POSTS.query.format(status, post_select_limit)
            logger.info(LogInfoMsg.MYSQL_QUERY.description.format(self.__log_id, self.__user_name, get_post_query))
            cursor = self.__cursor
            cursor.execute(get_post_query)
            columns = [item[0] for item in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_GET_POSTS_ERROR.description.format(self.__log_id, self.__user_name, e))
            raise e
        return data

    def get_faculty_list(self) -> List:
        try:
            get_faculty_list_query = MysqlQuery.GET_FACULTY_LIST.query
            logger.info(LogInfoMsg.MYSQL_QUERY.description.format(self.__log_id, self.__user_name,
                                                                  get_faculty_list_query))
            cursor = self.__cursor
            cursor.execute(get_faculty_list_query)
            columns = [item[0] for item in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_GET_FACULTY_LIST_ERROR.description.format(self.__log_id, self.__user_name,
                                                                                     e))
            raise e
        return data

    def get_field_of_study_list(self) -> List:
        try:
            get_field_of_study_list = MysqlQuery.GET_FILED_OF_STUDY_LIST.query
            logger.info(LogInfoMsg.MYSQL_QUERY.description.format(self.__log_id, self.__user_name,
                                                                  get_field_of_study_list))
            cursor = self.__cursor
            cursor.execute(get_field_of_study_list)
            columns = [item[0] for item in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_GET_FIELD_OF_STUDY_LIST_ERROR.description.format(self.__log_id,
                                                                                            self.__user_name, e))
            raise e
        return data

    def get_course(self) -> List:
        try:
            get_course_list = MysqlQuery.GET_COURSE_LIST.query
            logger.info(LogInfoMsg.MYSQL_QUERY.description.format(self.__log_id, self.__user_name,
                                                                  get_course_list))
            cursor = self.__cursor
            cursor.execute(get_course_list)
            columns = [item[0] for item in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_GET_COURSE_LIST_ERROR.description.format(self.__log_id, self.__user_name, e))
            raise e
        return data

    def change_password(self, user_email: str, new_password: str):
        try:
            change_password_query = MysqlQuery.CHANGE_USER_PASSWORD.query.format(new_password, user_email)
            logger.info(LogInfoMsg.MYSQL_QUERY.description.format(self.__log_id, self.__user_name,
                                                                  change_password_query))
            cursor = self.__cursor
            cursor.execute(change_password_query)
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_CHANGE_PASSWORD_ERROR.description.format(self.__log_id, user_email, e))
            raise e

    def upload_post(self, user_id: int, content: str, image_path: str):
        try:
            upload_post_query = MysqlQuery.UPLOAD_POST.query.format(user_id, content, get_current_date(), image_path,
                                                                    PostStatus.ACTIVE.get_description.lower())
            logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(upload_post_query))
            cursor = self.__cursor
            cursor.execute(upload_post_query)
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_UPLOAD_POST_ERROR.description.format(self.__log_id, user_id, e))
            raise e

    def activate_user(self, user_id: int):
        try:
            activate_user_query = MysqlQuery.ACTIVATE_USER.query.format(UserStatus.ACTIVE.get_description, user_id)
            logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(activate_user_query))
            cursor = self.__cursor
            cursor.execute(activate_user_query)
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_ACTIVATE_USER_ERROR.description.format(self.__log_id, user_id, e))
            raise e

    def get_comments(self, post_id: int) -> List:
        try:
            get_comments_query = MysqlQuery.GET_COMMENTS.query.format(post_id,
                                                                      PostStatus.ACTIVE.get_description.lower())
            logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(get_comments_query))
            cursor = self.__cursor
            cursor.execute(get_comments_query)
            columns = [item[0] for item in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_GET_COMMENTS_ERROR.description.format(self.__log_id, self.__user_name, e))
            raise e
        else:
            return data

    def upload_comment(self, user_id: str, content: str, post_id: int):
        try:
            upload_post_query = MysqlQuery.UPLOAD_COMMENT.query.format(user_id, content, get_current_date(), post_id,
                                                                       PostStatus.ACTIVE.get_description.lower())
            logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(upload_post_query))
            cursor = self.__cursor
            cursor.execute(upload_post_query)
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_UPLOAD_COMMENT_ERROR.description.format(self.__log_id, user_id, e))
            raise e

    def upload_product(self, upload_product_data: UploadProductData):
        try:
            upload_product_query = MysqlQuery.UPLOAD_PRODUCT_DATA.query.format(upload_product_data.productType,
                                                                               upload_product_data.title,
                                                                               upload_product_data.userId,
                                                                               get_current_date(),
                                                                               get_current_date(),
                                                                               ProductStatus.ACTIVE.
                                                                               get_description.lower(),
                                                                               upload_product_data.year,
                                                                               upload_product_data.fieldOfStudy,
                                                                               upload_product_data.price,
                                                                               upload_product_data.content,
                                                                               upload_product_data.image)
            logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(upload_product_query))
            cursor = self.__cursor
            cursor.execute(upload_product_query)
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_UPLOAD_POST_ERROR.description.format(self.__log_id, user_id, e))
            raise e

    def get_product_type(self) -> List:
        try:
            get_product_type_query = MysqlQuery.GET_PRODUCT_TYPE.query
            logger.info(LogInfoMsg.MYSQL_QUERY.description.format(self.__log_id, self.__user_name,
                                                                  get_product_type_query))
            cursor = self.__cursor
            cursor.execute(get_product_type_query)
            columns = [item[0] for item in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_GET_PRODUCT_TYPE.description.format(self.__log_id, self.__user_name, e))
            raise e
        return data

    def get_products(self, product_type: int, status: str) -> List:
        try:
            get_products_query = MysqlQuery.GET_PRODUCTS.query.format(product_type, status)
            logger.info(LogInfoMsg.MYSQL_QUERY.description.format(self.__log_id, self.__user_name, get_products_query))
            cursor = self.__cursor
            cursor.execute(get_products_query)
            columns = [item[0] for item in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_GET_POSTS_ERROR.description.format(self.__log_id, self.__user_name, e))
            raise e
        return data

    def filter_products(self, filter_products_data: FilterProductsData):
        try:
            filter = ''
            if filter_products_data.priceMax != '-1':
                filter = filter + f" and price < {filter_products_data.priceMax}"
            if filter_products_data.priceMin != '-1':
                filter = filter + f" and price > {filter_products_data.priceMin}"
            if filter_products_data.fieldOfStudyId != -1:
                filter = filter + f" and field_of_study_id = {filter_products_data.fieldOfStudyId}"
            if filter_products_data.yearOfStudy != '-1':
                filter = filter + f" and study_year = {filter_products_data.yearOfStudy}"
            if filter_products_data.title != '-1' and filter_products_data.title != '':
                filter = filter + f' and lower(prodcuts.name) like "{generate_title_filter(filter_products_data.title).lower()}"'
            if filter_products_data.uploadDate == 'Newest':
                order = 'desc'
            else:
                order = 'asc'
            filter_products_query = MysqlQuery.GET_FILTERED_PRODUCTS.query.format(filter_products_data.productType,
                                                                                  ProductStatus.ACTIVE.get_description
                                                                                  .lower(), filter, order)
            logger.info(LogInfoMsg.MYSQL_QUERY.description.format(self.__log_id, self.__user_name, filter_products_query))
            cursor = self.__cursor
            cursor.execute(filter_products_query)
            columns = [item[0] for item in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        except mysql.connector.Error as e:
            logger.error(LogErrorMsg.MYSQL_GET_POSTS_ERROR.description.format(self.__log_id, self.__user_name, e))
            raise e
        return data
