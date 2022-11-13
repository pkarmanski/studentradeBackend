import uuid
import random


def generate_token() -> str:
    return str(uuid.uuid4()).replace("-", "")


def generate_code() -> str:
    return str(random.randint(1000, 9999))
