from enum import Enum


class LogInfoMsg(Enum):
    CONNECTED_TO_MYSQL = 'session_id: {}, user: {} connected to mysql server'
    DISCONNECTED_FROM_MYSQL = 'session_id: {}, user: {} disconnected from mysql server'
    MYSQL_COMMIT_OPERATION = 'session_id: {}, user: {} everything committed on mysql server'
    MYSQL_QUERY = 'session_id: {}, user: {}, query: {}'
    SQLITE_CONNECTED_START = 'connected to sqlite'
    SQLITE_DISCONNECTED_START = 'disconnected from sqlite'
    SQLITE_CONNECTED = 'session_id: {}, user: {}, connected to sqlite'
    SQLITE_DISCONNECTED = 'session_id: {}, user: {}, disconnected from sqlite'
    SQLITE_QUERY_START = 'sqlite create login_users table query: {}'
    SQLITE_QUERY = 'session_id: {}, user: {}, query: {}'

    def __init__(self, description):
        self.__description = description

    @property
    def description(self) -> str:
        return self.__description
