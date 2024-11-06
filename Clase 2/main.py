# Clases en python
class Product:
    # Atributo name
    name = "Sillas"
    # Atributo privado (con doble guion bajo al comienzo)
    __cod_product = None

    # Getter y Setter
    def get_cod_product(self):
        return self.__cod_product

    def set_cod_product(self, cod_product: int):
        # Aqui ud puede programas reglas de negocio
        # Luego asignar el valor al atributo
        self.__cod_product = cod_product

# Instanciar clase Product
product = Product()

# Asignar codigo de producto al atributo cod_product del objeto producto
product.set_cod_product(5461)

# Intentar acceder al atributo cod_product que es privado
print(product.get_cod_product())
