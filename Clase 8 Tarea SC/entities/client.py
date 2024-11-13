class Client:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__id = None
        self.__email = None

    def get_id(self) -> int:
        return self.__id
    
    def set_id(self, id: int) -> None:
        # TODO: Agregar validacion para asegurar que parametro Id sea entero.
        self.__id = id
    
    def get_email(self) -> str:        
        return self.__email
    
    def set_email(self, email: str) -> None:
        # TODO: Implementar validacion de formato de email.
        self.__email = email