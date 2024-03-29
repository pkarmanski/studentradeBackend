from enum import Enum


class PostStatus(Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"

    def __init__(self, description: str):
        self.__description = description

    @property
    def get_description(self):
        return self.__description


class ProductStatus(Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"

    def __init__(self, description: str):
        self.__description = description

    @property
    def get_description(self):
        return self.__description


class UserStatus(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


    def __init__(self, description: str):
        self.__description = description

    @property
    def get_description(self):
        return self.__description
