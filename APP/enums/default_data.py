from enum import Enum


class   `DefaultValues(Enum):
    token_default = '-1'

    def __init__(self, default: str):
        self.__default = default

    @property
    def default(self):
        return self.__default
