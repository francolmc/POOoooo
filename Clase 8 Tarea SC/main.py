from entities.product import Product
from entities.shopping_cart import ShoppingCart

polo = Product("Polo")
polo.set_id(1)
polo.add_stock(4)
polo.set_price(15000)

celular = Product("Celular")
polo.set_id(2)
celular.add_stock(10)
celular.set_price(400000)

zapatilla = Product("Zapatilla")
polo.set_id(3)
zapatilla.add_stock(2)
zapatilla.set_price(95000)

carrito = ShoppingCart()
carrito.set_id(1)
carrito.add_product(zapatilla, 1)
carrito.add_product(polo, 2)

print(carrito.get_total())

carrito.show_detail()