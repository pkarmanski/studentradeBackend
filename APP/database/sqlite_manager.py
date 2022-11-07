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
            exit(2)


def insert_user(db_file: str, log_id: str, user_id: str, ip: str, temporary_id: str):
    try:
        con = sqlite3.connect(db_file)
        logger.info(LogInfoMsg.SQLITE_CONNECTED.description.format(log_id, user_id))
    except sqlite3.Error as e:
        logger.error(LogErrorMsg.SQLITE_CONNECTION_ERROR.description.format(e))
        raise e
    else:
        try:
            insert_user_query = SqliteQuery.insert_user.query.format(user_id, str(int(time.time())), ip, temporary_id)
            logger.info(LogInfoMsg.SQLITE_QUERY_START.description.format(insert_user_query))
            cursor = con.cursor()
            cursor.execute(insert_user_query)
            con.commit()
            cursor.close()
            con.close()
        except sqlite3.Error as e:
            logger.error(LogErrorMsg.SQLITE_QUERY_START_ERROR.description.format(log_id, user_id, e))
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
            select_user_query= SqliteQuery.select_user.query.format(temporary_id)
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


