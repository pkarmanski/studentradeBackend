from enum import Enum


class LogErrorMsg(Enum):
    MYSQL_CONNECTION_ERROR = 'session_id: {}, user: {}, failed to connect to mysql server, error: {}'
    MYSQL_CHECK_USER_BY_LOGIN_ERROR = 'session_id: {}, user: {}, failed to check user by login, error: {}'
    MYSQL_CHECK_USER_BY_EMAIL_ERROR = 'session_id: {}, user: {}, failed to check user by email, error: {}'
    MYSQL_REGISTER_USER_ERROR = 'session_id: {}, user: {}, failed to register user, error: {}'
    MYSQL_LOGIN_USER_ERROR = 'session_id: {}, user: {}, failed to login user, error: {}'

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
