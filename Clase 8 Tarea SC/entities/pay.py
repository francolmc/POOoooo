from entities.shopping_cart import ShoppingCart

class Pay:
    def __init__(self) -> None:
        self.__id = None
        self.__payment_date = None
        self.__shopping_cart = None
    
    def get_id(self) -> int:
        return self.__id
    
    def set_id(self, id: int) -> None:
        self.__id = id

    def get_payment_date(self) -> int:
        return self.__payment_date
    
    def set_payment_date(self, payment_date: int) -> None:
        self.__payment_date = payment_date

    def get_shopping_cart(self) -> int:
        return self.__shopping_cart
    
    def set_shopping_cart(self, shopping_cart: ShoppingCart) -> None:
        self.__shopping_cart = shopping_cart