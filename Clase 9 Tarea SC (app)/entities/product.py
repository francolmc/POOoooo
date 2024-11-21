from utils.uuid_code import is_valid_uuid

class Product:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__id = None
        self.__price = None
        self.__stock = 0

    def get_id(self) -> int:
        return self.__id
    
    def set_id(self, id: int) -> None:
        if (is_valid_uuid(id)):
            self.__id = id
        else:
            raise ValueError("El id debe tener un formato valido UUID")

    def get_price(self) -> int:
        return self.__price
    
    def set_price(self, price: int) -> None:
        if (isinstance(price, int)):
            self.__price = price
        elif (price <= 0):
            raise ValueError("El precio debe ser mayor a 0")
        else:
            raise ValueError("El precio debe ser un entero")
        

    def get_stock(self) -> int:
        return self.__stock
    
    def add_stock(self, stock: int) -> None:
        if (stock < 0):
            raise ValueError("El stock debe ser mayor a 0")
        else:
            self.__stock = self.__stock + stock
    
    def remove_stock(self, stock: int) -> None:
        if (self.__stock < stock):
            raise ValueError("No hay stock suficiente.")
        else:
            self.__stock = self.__stock - stock

    