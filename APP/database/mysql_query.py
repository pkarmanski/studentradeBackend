from enum import Enum


class MysqlQuery(Enum):
    CHECK_USER_EXISTENCE_BY_LOGIN = 'select login from users where login = "{}"'
    CHECK_USER_EXISTENCE_BY_EMAIL = 'select email from users where email = "{}"'
    REGISTER_USER = 'insert into users (login, password, email, faculty_id) values("{}","{}", "{}", {})'

    def __init__(self, query: str):
        self.__query = query

    @property
    def query(self):
        return self.__query
