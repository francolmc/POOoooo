from entities.product import Product
from entities.shopping_cart import ShoppingCart
from utils.seeder import zapatilla, polo, celular

carrito = ShoppingCart()
carrito.set_id(1)
carrito.add_product(zapatilla, 1)
carrito.add_product(polo, 2)

print(carrito.get_total())

carrito.show_detail()