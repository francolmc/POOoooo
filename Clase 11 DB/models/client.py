class Client:
    def __init__(self) -> None:
        # TODO: Agregar el atributo id
        self.__name: str = ""
        self.__email: str = ""
    
    def get_name(self) -> str:
        return self.__name
    
    def set_name(self, name: str):
        self.__name = name

    def get_email(self) -> str:
        return self.__email
    
    def set_email(self, email: str):
        self.__email = email