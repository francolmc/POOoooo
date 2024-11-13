class Product:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__id = None
        self.__price = None
        self.__stock = 0

    def get_id(self) -> int:
        return self.__id
    
    def set_id(self, id: int) -> None:
        self.__id = id

    def get_price(self) -> int:
        return self.__price
    
    def set_price(self, price: int) -> None:
        self.__price = price

    def get_stock(self) -> int:
        return self.__stock
    
    def add_stock(self, stock: int) -> None:
        # TODO: Controlar la existencia del stock
        self.__stock = self.__stock + stock
    
    def remove_stock(self, stock: int) -> None:
        # TODO: Controlar la existencia del stock
        self.__stock = self.__stock - stock

    