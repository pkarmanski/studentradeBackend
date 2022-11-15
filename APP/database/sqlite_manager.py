import sqlite3
import logging
from APP.database.sqlite_query import SqliteQuery
from APP.messages.error_msg import ServiceErrorMsg, LogErrorMsg
from APP.messages.info_msg import LogInfoMsg
import time
from typing import List

logger = logging.getLogger(__name__)


def create_logged_user_table(db_file: str):
    try:
        con = sqlite3.connect(db_file)
        logger.info(LogInfoMsg.SQLITE_CONNECTED_START.description)
    except sqlite3.Error as e:
        logger.error(LogErrorMsg.SQLITE_CONNECTION_ERROR.description.format(e))
        time.sleep(5)
        exit(1)
    else:
        try:
            create_table_query = SqliteQuery.create_table.query
            logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(create_table_query))
            cursor = con.cursor()
            cursor.execute(create_table_query)
            con.commit()
            cursor.close()
            con.close()
        except sqlite3.Error as e:
            logger.error(LogErrorMsg.SQLITE_QUERY_START_ERROR.description.format(e))
            time.sleep(5)
            exit(2)


def create_forgot_password_table(db_file: str):
    try:
        con = sqlite3.connect(db_file)
        logger.info(LogInfoMsg.SQLITE_CONNECTED_START.description)
    except sqlite3.Error as e:
        logger.error(LogErrorMsg.SQLITE_CONNECTION_ERROR.description.format(e))
        time.sleep(5)
        exit(3)
    else:
        try:
            create_table_query = SqliteQuery.create_table_forgot_password.query
            logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(create_table_query))
            cursor = con.cursor()
            cursor.execute(create_table_query)
            con.commit()
            cursor.close()
            con.close()
        except sqlite3.Error as e:
            logger.error(LogErrorMsg.SQLITE_QUERY_START_ERROR.description.format(e))
            time.sleep(5)
            exit(4)


def create_activate_user_table(db_file: str):
    try:
        con = sqlite3.connect(db_file)
        logger.info(LogInfoMsg.SQLITE_CONNECTED_START.description)
    except sqlite3.Error as e:
        logger.error(LogErrorMsg.SQLITE_CONNECTION_ERROR.description.format(e))
        time.sleep(5)
        exit(5)
    else:
        try:
            create_table_query = SqliteQuery.create_table_activate_user.query
            logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(create_table_query))
            cursor = con.cursor()
            cursor.execute(create_table_query)
            con.commit()
            cursor.close()
            con.close()
        except sqlite3.Error as e:
            logger.error(LogErrorMsg.SQLITE_QUERY_START_ERROR.description.format(e))
            time.sleep(5)
            exit(6)


def insert_user(db_file: str, log_id: str, user_id: str, ip: str, temporary_id: str, login: str):
    try:
        con = sqlite3.connect(db_file)
        logger.info(LogInfoMsg.SQLITE_CONNECTED.description.format(log_id, user_id))
    except sqlite3.Error as e:
        logger.error(LogErrorMsg.SQLITE_CONNECTION_ERROR.description.format(e))
        raise e
    else:
        try:
            insert_user_query = SqliteQuery.insert_user.query.format(user_id, str(int(time.time())), ip, temporary_id,
                                                                     login)
            logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(insert_user_query))
            cursor = con.cursor()
            cursor.execute(insert_user_query)
            con.commit()
            cursor.close()
            con.close()
        except sqlite3.Error as e:
            logger.error(LogErrorMsg.SQLITE_QUERY_START_ERROR.description.format(log_id, user_id, e))
            raise e


def insert_user_forgot_password(db_file: str, log_id: str, user_email: str, code: str):
    try:
        con = sqlite3.connect(db_file)
        logger.info(LogInfoMsg.SQLITE_CONNECTED.description.format(log_id, user_email))
    except sqlite3.Error as e:
        logger.error(LogErrorMsg.SQLITE_CONNECTION_ERROR.description.format(e))
        raise e
    else:
        try:
            insert_user_query = SqliteQuery.insert_user_forgot_password.query.format(user_email, code, str(int(time.time())))
            logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(insert_user_query))
            cursor = con.cursor()
            cursor.execute(insert_user_query)
            con.commit()
            cursor.close()
            con.close()
        except sqlite3.Error as e:
            logger.error(LogErrorMsg.SQLITE_QUERY_START_ERROR.description.format(log_id, user_email, e))
            raise e


def insert_user_to_activate(db_file: str, log_id: str, user_id: int, token: str, code: str):
    try:
        con = sqlite3.connect(db_file)
        logger.info(LogInfoMsg.SQLITE_CONNECTED.description.format(log_id, user_id))
    except sqlite3.Error as e:
        logger.error(LogErrorMsg.SQLITE_CONNECTION_ERROR.description.format(e))
        raise e
    else:
        try:
            insert_activate_user = SqliteQuery.insert_user_to_activate.query.format(token, code, user_id,
                                                                                    str(int(time.time())))
            logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(insert_activate_user))
            cursor = con.cursor()
            cursor.execute(insert_activate_user)
            con.commit()
            cursor.close()
            con.close()
        except sqlite3.Error as e:
            logger.error(LogErrorMsg.SQLITE_INSERT_ERROR.description.format(log_id, token, e))
            raise e


def update_user(db_file: str, log_id: str, user_id: str, temporary_id: str):
    try:
        con = sqlite3.connect(db_file)
        logger.info(LogInfoMsg.SQLITE_CONNECTED.description.format(log_id, user_id))
    except sqlite3.Error as e:
        logger.error(LogErrorMsg.SQLITE_CONNECTION_ERROR.description.format(e))
        raise e
    else:
        try:
            update_user_query = SqliteQuery.update_user.query.format(str(int(time.time())), temporary_id, user_id)
            logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(update_user_query))
            cursor = con.cursor()
            cursor.execute(update_user_query)
            con.commit()
            cursor.close()
            con.close()
        except sqlite3.Error as e:
            logger.error(LogErrorMsg.SQLITE_UPDATE_ERROR.description.format(log_id, user_id, e))
            raise e


def select_user(db_file: str, log_id: str, temporary_id: str) -> List:
    try:
        con = sqlite3.connect(db_file)
        logger.info(LogInfoMsg.SQLITE_CONNECTED.description.format(log_id, temporary_id))
    except sqlite3.Error as e:
        logger.error(LogErrorMsg.SQLITE_CONNECTION_ERROR.description.format(e))
        raise e
    else:
        try:
            select_user_query = SqliteQuery.select_user.query.format(temporary_id)
            logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(select_user_query))
            cursor = con.cursor()
            cursor.execute(select_user_query)
            columns = [item[0] for item in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            con.commit()
            cursor.close()
            con.close()
        except sqlite3.Error as e:
            logger.error(LogErrorMsg.SQLITE_UPDATE_ERROR.description.format(log_id, temporary_id, e))
            raise e
    return data


def select_forgot_code(db_file: str, log_id: str, user_email: str) -> List:
    try:
        con = sqlite3.connect(db_file)
        logger.info(LogInfoMsg.SQLITE_CONNECTED.description.format(log_id, user_email))
    except sqlite3.Error as e:
        logger.error(LogErrorMsg.SQLITE_CONNECTION_ERROR.description.format(e))
        raise e
    else:
        try:
            select_user_query = SqliteQuery.select_forgot_code.query.format(user_email)
            logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(select_user_query))
            cursor = con.cursor()
            cursor.execute(select_user_query)
            columns = [item[0] for item in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            con.commit()
            cursor.close()
            con.close()
            logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(data))

        except sqlite3.Error as e:
            logger.error(LogErrorMsg.SQLITE_UPDATE_ERROR.description.format(log_id, user_email, e))
            raise e
    return data


def select_activate_user(db_file: str, log_id: str, token: str, code: str) -> List:
    try:
        con = sqlite3.connect(db_file)
        logger.info(LogInfoMsg.SQLITE_CONNECTED.description.format(log_id, token))
    except sqlite3.Error as e:
        logger.error(LogErrorMsg.SQLITE_CONNECTION_ERROR.description.format(e))
        raise e
    else:
        try:
            select_activate_user_query = SqliteQuery.select_activate_user_code.query.format(token, code)
            logger.info(LogInfoMsg.SQLITE_QUERY.description.format(log_id, token, select_activate_user_query))
            cursor = con.cursor()
            cursor.execute(select_activate_user_query)
            columns = [item[0] for item in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            con.commit()
            cursor.close()
            con.close()
        except sqlite3.Error as e:
            logger.error(LogErrorMsg.SQLITE_UPDATE_ERROR.description.format(log_id, token, e))
            raise e
    return data


def delete_user(db_file: str, token_lifetime: str):
    try:
        con = sqlite3.connect(db_file)
        logger.info(LogInfoMsg.SQLITE_CONNECTED_START.description)
    except sqlite3.Error as e:
        logger.error(LogErrorMsg.SQLITE_CONNECTION_ERROR.description.format(e))
        raise e
    else:
        try:
            delete_user_query = SqliteQuery.delete_user.query.format(str(int(time.time())), token_lifetime)
            # logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(delete_user_query))
            cursor = con.cursor()
            cursor.execute(delete_user_query)
            con.commit()
            cursor.close()
            con.close()
        except sqlite3.Error as e:
            logger.error(LogErrorMsg.SQLITE_DELETE_ERROR.description.format(e))
            raise e


def delete_forgot_user(db_file: str, user_email: str):
    try:
        con = sqlite3.connect(db_file)
        logger.info(LogInfoMsg.SQLITE_CONNECTED_START.description)
    except sqlite3.Error as e:
        logger.error(LogErrorMsg.SQLITE_CONNECTION_ERROR.description.format(e))
        raise e
    else:
        try:
            delete_user_query = SqliteQuery.delete_forgot_user.query.format(user_email)
            # logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(delete_user_query))
            cursor = con.cursor()
            cursor.execute(delete_user_query)
            con.commit()
            cursor.close()
            con.close()
        except sqlite3.Error as e:
            logger.error(LogErrorMsg.SQLITE_DELETE_ERROR.description.format(e))
            raise e


def delete_forgot_user_overtime(db_file: str, code_time: str):
    try:
        con = sqlite3.connect(db_file)
        logger.info(LogInfoMsg.SQLITE_CONNECTED_START.description)
    except sqlite3.Error as e:
        logger.error(LogErrorMsg.SQLITE_CONNECTION_ERROR.description.format(e))
        raise e
    else:
        try:
            delete_code_query = SqliteQuery.delete_forgot_user_overtime.query.format(str(int(time.time())), code_time)
            # logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(delete_code_query))
            cursor = con.cursor()
            cursor.execute(delete_code_query)
            con.commit()
            cursor.close()
            con.close()
        except sqlite3.Error as e:
            logger.error(LogErrorMsg.SQLITE_DELETE_ERROR.description.format(e))
            raise e


def select_all(db_file: str) -> List:
    try:
        con = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        logger.error(LogErrorMsg.SQLITE_CONNECTION_ERROR.description.format(e))
        raise e
    else:
        try:
            select_user_query = "select * from logged_users"
            logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(select_user_query))
            cursor = con.cursor()
            cursor.execute(select_user_query)
            columns = [item[0] for item in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            logger.critical(data)
            con.commit()
            cursor.close()
            con.close()
        except sqlite3.Error as e:
            raise e
    return data
