import sqlite3
import threading
import time
from APP.database.sqlite_manager import delete_user, delete_forgot_user_overtime


def background(f):
    def background_func(*a, **kw):
        threading.Thread(target=f, args=a, kwargs=kw).start()
    return background_func


@background
def check_token_lifetime(db_file: str, token_lifetime: str, code_lifetime: str, interval: int):
    while True:
        try:
            delete_user(db_file, token_lifetime)
            delete_forgot_user_overtime(db_file, code_lifetime)
        except sqlite3.Error:
            pass
        time.sleep(interval)


