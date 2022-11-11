from enum import Enum


class SqliteQuery(Enum):
    create_table = 'create table logged_users (id int auto_increment primary key, user_id int, temporary_id varchar(150), login_time varchar(50), ip varchar(30))'
    create_table_forgot_password = 'create table forgot_password (id int auto_increment primary key, user_email varchar(150), code int, confirmation_time varchar(50)'
    insert_user = 'insert into logged_users (user_id, login_time, ip, temporary_id) values("{}", "{}", "{}", "{}")'
    insert_user_forgot_password = 'insert into forgot_password (user_email, code, confirmation_time) values("{}", "{}", "{}")'

    select_user = 'select user_id from logged_users where temporary_id="{}"'
    select_forgot_code = 'select code from logged_users where email = "{}"'
    update_user = 'update logged_users set login_time="{}", temporary_id="{}" where user_id="{}"'
    delete_user = 'delete from logged_users where "{}" - login_time > {}'
    delete_forgot_user = 'delete from forgot_password where email = "{}"'

    def __init__(self, query: str):
        self.__query = query

    @property
    def query(self):
        return self.__query