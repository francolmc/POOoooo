from entities.product import Product
from utils.uuid_code import is_valid_uuid

class ShoppingCart:
    def __init__(self) -> None:
        self.__id = None
        self.__shopping_cart_date = None
        self.__products = []

    def get_id(self) -> int:
        return self.__id
    
    def set_id(self, id: int) -> None:
        if (is_valid_uuid(id)):
            self.__id = id
        else:
            raise ValueError("El id debe tener un formato valido UUID")

    def add_product(self, product: Product, quantity: int) -> None:
        if (product.get_stock() < quantity):
            raise ValueError("No hay stock suficiente")
        else:
            self.__products.append({
                "product": product,
                "quantity": quantity
            })
            product.remove_stock(quantity)

    def remove_product(self, index: int) -> None:
        self.__products[index]["product"].add_stock(self.__products[index]["quantity"])
        self.__products.pop(index)


    def get_total(self) -> int:
        grand_total = 0
        for item in self.__products:
            product: Product = item["product"]
            quantity: int = item["quantity"]
            grand_total = grand_total + (quantity * product.get_price())
        return grand_total

    def show_detail(self) -> None:
        index = 1
        for item in self.__products:
            product: Product = item["product"]
            quantity: int = item["quantity"]
            print(f'{index}, Producto: {product.name}, Cantidad: {quantity}, Total: {quantity * product.get_price()}')
            index = index + 1