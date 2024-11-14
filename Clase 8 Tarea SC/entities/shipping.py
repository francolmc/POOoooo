from entities.status import Status

class Shipping:
    def __init__(self) -> None:
        self.__id = None
        self.address = None
        self.__shipping_date = None
        self.__delivery_date = None
        # TODO: Implementar enum del status
        self.__status = None
        # TODO: Relacionar el atributo __shopping_cart con la clase ShoppingCart
        self.shopping_cart = None

    def get_id(self) -> int:
        return self.__id
    
    def set_id(self, id: int) -> None:
        self.__id = id

    def get_shipping_date(self) -> int:
        return self.__shipping_date
    
    def set_shipping_date(self, shipping_date: str) -> None:
        # TODO: Validar el formato de fecha ingresado YYYY-MM-DD
        self.__shipping_date = shipping_date

    def get_delivery_date(self) -> int:
        return self.__delivery_date
    
    def set_delivery_date(self, delivery_date: str) -> None:
        # TODO: Validar el formato de fecha ingresado YYYY-MM-DD
        self.__delivery_date = delivery_date

    def get_status(self) -> Status:
        return self.__status
    
    def set_status(self, status: Status):
        self.__status = status