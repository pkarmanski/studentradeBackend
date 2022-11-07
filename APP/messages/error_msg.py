from enum import Enum


class LogErrorMsg(Enum):
    MYSQL_CONNECTION_ERROR = 'session_id: {}, user: {}, failed to connect to mysql server, error: {}'
    MYSQL_CHECK_USER_BY_LOGIN_ERROR = 'session_id: {}, user: {}, failed to check user by login, error: {}'
    MYSQL_CHECK_USER_BY_EMAIL_ERROR = 'session_id: {}, user: {}, failed to check user by email, error: {}'
    MYSQL_REGISTER_USER_ERROR = 'session_id: {}, user: {}, failed to register user, error: {}'
    MYSQL_LOGIN_USER_ERROR = 'session_id: {}, user: {}, failed to login user, error: {}'
    MYSQL_GET_POSTS_ERROR = 'session_id: {}, user: {}, failed to get post, error: {}'
    MYSQL_GET_FACULTY_LIST_ERROR = 'session_id: {}, user: {}, failed to get faculty list, error: {}'
    MYSQL_GET_FIELD_OF_STUDY_LIST_ERROR = 'session_id: {}, user: {}, failed to get field of study list, error: {}'
    MYSQL_GET_COURSE_LIST_ERROR = 'session_id: {}, user: {}, failed to get course list, error: {}'
    SQLITE_CONNECTION_ERROR = 'failed to connected to sqlite, error: {}'
    SQLITE_DISCONNECTED_ERROR = 'failed to disconnected from sqlite'
    SQLITE_QUERY_START_ERROR = 'sqlite failed to create login_users table error: {}'
    SQLITE_QUERY_ERROR = 'session_id: {}, user: {}, error: {}'
    SQLITE_INSERT_ERROR = 'session_id: {}, user: {}, failed to insert user, error: {}'
    SQLITE_UPDATE_ERROR = 'session_id: {}, user: {}, failed to update user, error: {}'
    SQLITE_SELECT_ERROR = 'session_id: {}, user: {}, failed to select user, error: {}'
    SQLITE_DELETE_ERROR = 'failed to delete user, error: {}'

    def __init__(self, description: str):
        self.__description = description

    @property
    def description(self) -> str:
        return self.__description


class ServiceErrorMsg(Enum):
    EVERYTHING_OK = ('EVERYTHING_OK', 0)
    MYSQL_CONNECTION_ERROR = ('MYSQL_CONNECTION_ERROR', 100)
    USER_LOGIN_EXISTS = ('USER_LOGIN_EXISTS', 101)
    USER_EMAIL_EXISTS = ('USER_EMAIL_EXISTS', 102)
    REGISTER_USER_ERROR = ('ERROR_OCCURRED_DURING_REGISTRATION', 103)
    LOGIN_USER_ERROR = ('ERROR_OCCURRED_DURING_REGISTRATION', 104)
    USER_NOT_EXISTS = ('USER_DOES_NOT_EXISTS', 105)
    GET_POSTS_ERROR = ('FAILED_TO_GET_POSTS', 106)
    GET_FACULTY_ERROR = ('FAILED_TO_GET_FACULTY_LIST', 107)
    GET_FILED_OF_STUDY_ERROR = ('FAILED_TO_GET_FIELD_OF_STUDY_LIST', 108)
    GET_COURSE_ERROR = ('FAILED_TO_GET_COURSE_LIST', 109)
    SQLITE_INSERT_ERROR = ('FAILED_TO_INSERT_USER', 110)
    SQLITE_SELECT_ERROR = ('FAILED_TO_SELECT_USER', 111)
    SQLITE_UPDATE_ERROR = ('FAILED_TO_UPDATE_USER', 113)



    def __init__(self, description: str, error_id: int):
        self.__description = description
        self.__error_id = error_id

    @property
    def description(self) -> str:
        return self.__description

    @property
    def error_id(self) -> int:
        return self.__error_id


class YamlErrorMsg(Enum):
    YAML_FILE_NOT_FOUND = 'yaml file is missing default name: config.yaml'

    def __init__(self, description):
        self.__description = description

    @property
    def description(self) -> str:
        return self.__description
