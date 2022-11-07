from enum import Enum


class SqliteQuery(Enum):
    create_table = 'create table logged_users (id int autoincrement primary key, user_id int, temporary_id varchar(150), login_time datetime, ip varchar(30))'
    insert_user = 'insert into logged_users (user_id, login_time, ip, temporary_id) values("{}", "{}", "{}", "{}")'
    select_user = 'select user_id from logged_users where temporary_id="{}"'
    update_user = 'update logged_users set login_time="{}", temporary_id="{}" where user_id="{}"'

    def __init__(self, query: str):
        self.__query = query

    @property
    def query(self):
        return self.__query

