from entities.shopping_cart import ShoppingCart
import re
from utils.uuid_code import generate_uuid, is_valid_uuid

class Client:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__id = None
        self.__email = None
        self.__carts: list[ShoppingCart] = []

    def get_id(self) -> int:
        return self.__id
    
    def set_id(self, id: int) -> None:
        if (is_valid_uuid(id)):
            self.__id = id
        else:
            raise ValueError("El id debe tener un formato valido UUID")
    
    def get_email(self) -> str:        
        return self.__email
    
    def set_email(self, email: str) -> None:
        if (re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)):
            self.__email = email
        else:
            raise ValueError("El email no es válido")

    def create_shopping_cart(self) -> ShoppingCart:
        shopping_cart = ShoppingCart()
        shopping_cart.set_id(generate_uuid())
        self.__carts.append(shopping_cart)
        return shopping_cart