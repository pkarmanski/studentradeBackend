class DatabaseParams:
    def __init__(self, host: str, port: int, login: str, password: str, database: str):
        self.__host = host
        self.__port = port
        self.__login = login
        self.__password = password
        self.__database = database

    @property
    def host(self) -> str:
        return self.__host

    @property
    def port(self) -> int:
        return self.__port

    @property
    def login(self) -> str:
        return self.__login

    @property
    def password(self) -> str:
        return self.__password

    @property
    def database(self) -> str:
        return self.__database
