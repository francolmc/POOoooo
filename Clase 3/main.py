# Clases en python
class Product:
    # Constructor de la clase
    # El constructor puede tener parametros entrada
    # En el caso que necesitemos un parametro opcionar, debe tener un valor por defecto, como name: str = None
    # si no especificamos un valor por defecto, el parametro sera obligatorio
    def __init__(self, name: str = None) -> None:
        # Atributo name
        self.name = name
        # Atributo privado (con doble guion bajo al comienzo)
        self.__cod_product = None

    # Getter y Setter
    def get_cod_product(self) -> int:
        return self.__cod_product

    def set_cod_product(self, cod_product: int) -> None:
        # Aqui ud puede programas reglas de negocio
        # Luego asignar el valor al atributo
        self.__cod_product = cod_product

# Instanciar clase Product
product = Product()

# Asignar codigo de producto al atributo cod_product del objeto producto
product.set_cod_product(5461)

# Intentar acceder al atributo cod_product que es privado
print(product.get_cod_product())
