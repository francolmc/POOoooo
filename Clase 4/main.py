from classes.chair import Chair

# Instanciar la clase Chair, que es una clase hija que hereda de Product
chair = Chair("Silla")
# Hacer uso del metodo set_cod_product que es propio de la clase padre Product
# y por herencia la podemos utilizar desde el objeto chair
chair.set_cod_product(890)

# Imprimimos los valores del objeto chair, haciendo uso de los atributos y metodos propios de
# la clase Product
print(f"El producto: {chair.name}, con codigo: {chair.get_cod_product()}")