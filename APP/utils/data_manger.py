import uuid
import random
import datetime
from typing import Union
import base64


def generate_token() -> str:
    return str(uuid.uuid4()).replace("-", "")


def generate_code() -> str:
    return str(random.randint(1000, 9999))


def get_current_date() -> str:
    return str(datetime.datetime.now()).split('.')[0]


def save_file(image: Union[bytes, str], file_name: str, extension: str, path: str) -> str:
    main_path = str(path + "/" + file_name + "." + extension).replace("//", "/")
    if isinstance(image, bytes):
        with open(main_path, "wb") as f:
            f.write(image)
            f.close()
    else:
        with open(main_path, "wb") as f:
            f.write(base64.b64decode(image))
            f.close()
    return main_path


def generate_link(token: str, code: str):
    return "http://localhost:8081/studentrade_v3_war_exploded/login/" + token + "/" + code

