class Product:
    def __init__(self, name: str = None) -> None:
        self.name = name
        self.__cod_product = None
    
    def get_cod_product(self) -> int:
        return self.__cod_product
    
    def set_cod_product(self, cod_product: int) -> None:
        self.__cod_product = cod_product

    # Creamos metodo para envio de producto sin implementar, ya que los productos
    # pueden realizar el envio de distintas formas.
    def send_product(self) -> None:
        pass