from entities.status import Status
from entities.shopping_cart import ShoppingCart
import re
from utils.uuid_code import is_valid_uuid

class Shipping:
    def __init__(self) -> None:
        self.__id = None
        self.address = None
        self.__shipping_date = None
        self.__delivery_date = None
        self.__status = None
        self.__shopping_cart = None

    def get_id(self) -> int:
        return self.__id
    
    def set_id(self, id: int) -> None:
        if (is_valid_uuid(id)):
            self.__id = id
        else:
            raise ValueError("El id debe tener un formato valido UUID")

    def get_shipping_date(self) -> int:
        return self.__shipping_date
    
    def set_shipping_date(self, shipping_date: str) -> None:
        if re.match(r'^\d{4}-\d{2}-\d{2}$', shipping_date):
            self.__shipping_date = shipping_date
        else:
            raise ValueError("El formato de la fecha debe ser YYYY-MM-DD")

    def get_delivery_date(self) -> int:
        return self.__delivery_date
    
    def set_delivery_date(self, delivery_date: str) -> None:
        if re.match(r'^\d{4}-\d{2}-\d{2}$', delivery_date):
            self.__delivery_date = delivery_date
        else:
            raise ValueError("El formato de la fecha debe ser YYYY-MM-DD")

    def get_status(self) -> Status:
        return self.__status
    
    def set_status(self, status: Status):
        self.__status = status

    def get_shopping_cart(self) -> ShoppingCart:
        return self.__shopping_cart
    
    def set_shopping_cart(self, shopping_cart: ShoppingCart):
        if (isinstance(shopping_cart, ShoppingCart)):
            self.__shopping_cart = shopping_cart
        else:
            raise ValueError("El shopping cart debe ser una instancia de ShoppingCart")