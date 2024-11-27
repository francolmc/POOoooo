class Client:
    def __init__(self) -> None:
        self.__id: int = -1
        self.__name: str = ""
        self.__email: str = ""
        self.__password: str = ""
    
    def get_id(self):
        return self.__id
    
    def set_id(self, id: int):
        self.__id = id

    def get_name(self) -> str:
        return self.__name
    
    def set_name(self, name: str):
        self.__name = name

    def get_email(self) -> str:
        return self.__email
    
    def set_email(self, email: str):
        self.__email = email

    def get_password(self) -> str:
        return self.__password
    
    def set_password(self, password: str) -> None:
        self.__password = password