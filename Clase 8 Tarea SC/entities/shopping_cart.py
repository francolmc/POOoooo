from entities.product import Product

class ShoppingCart:
    def __init__(self) -> None:
        self.__id = None
        self.__shopping_cart_date = None
        self.__products = []

    def get_id(self) -> int:
        return self.__id
    
    def set_id(self, id: int) -> None:
        self.__id = id

    def add_product(self, product: Product, quantity: int) -> None:
        # TODO: Agregar validacion de stock antes de agregar el producto a la lista
        self.__products.append({
            "product": product,
            "quantity": quantity
        })

    def remove_product(self, index: int) -> None:
        self.__products.pop(index)


    def get_total(self) -> int:
        grand_total = 0
        for product in self.__products:
            grand_total = grand_total + (product["quantity"] * product["product"].get_price())
        return grand_total

    def show_detail(self) -> None:
        index = 1
        for product in self.__products:
            print(f'{index}, Producto: {product["product"].name}, Cantidad: {product["quantity"]}, Total: {product["quantity"] * product["product"].get_price()}')
            index = index + 1