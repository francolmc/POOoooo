from classes.product import Product

class License(Product):
    def __init__(self, name: str = None) -> None:
        super().__init__(name)

    # Sobreescribimos el metodo enviar producto para el caso de productos digitales
    # los cuales seran enviador por correo.
    def send_product(self) -> None:
        print("Enviar correo electronico con el producto")