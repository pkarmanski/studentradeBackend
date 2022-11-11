from enum import Enum


class MysqlQuery(Enum):
    CHECK_USER_EXISTENCE_BY_LOGIN = 'select login from users where login = "{}"'
    CHECK_USER_EXISTENCE_BY_EMAIL = 'select email from users where email = "{}"'
    REGISTER_USER = 'insert into users (login, password, email, faculty_id) values("{}","{}", "{}", {})'
    LOGIN_USER = 'select id from users where login="{}" and password="{}"'
    GET_POSTS = 'select id, content, image from post where status="{}" order by upload_date limit {}'
    GET_FACULTY_LIST = 'select id, name from faculty'
    GET_FILED_OF_STUDY_LIST = 'select id, name from field_of_study'
    GET_COURSE_LIST = 'select id, name from course'
    CHANGE_USER_PASSWORD = 'update users set password = "{}" where email = "{}"'

    def __init__(self, query: str):
        self.__query = query

    @property
    def query(self):
        return self.__query
