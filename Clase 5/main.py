from classes.product import Product
from classes.chair import Chair
from classes.license import License

# metodo para enviar productos, sin especificar el tipo
def enviar(producto: Product) -> None:
    # Se ejecuta el metodo send_producto de la clase padre,
    # pero se ejecutara el metodo de cada sub clase.
    producto.send_product()


silla = Chair("Silla")
license = License("Windows 11")

enviar(silla)
enviar(license)



