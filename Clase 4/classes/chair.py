from classes.product import Product

# Para representar la herencia, se especifica la padre entre parentesis
class Chair(Product):
    def __init__(self, name: str = None) -> None:
        super().__init__(name)