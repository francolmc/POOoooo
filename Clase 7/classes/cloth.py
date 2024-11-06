from classes.product import Product

class Cloth (Product):
    def __init__(self, name: str = None) -> None:
        super().__init__(name)
        self.__size = None

    def send_product(self) -> None:
        print("Preparar caja para envio")
    
    # Definir los metodos set_size y get_size como propiedades 
    @property
    def size(self) -> str:
        return self.__size
    
    @size.setter
    def size(self, size: str) -> None:
        self.__size = size
    
    