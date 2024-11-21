from entities.product import Product
from utils.uuid_code import generate_uuid

polo = Product("Polo")
polo.set_id(generate_uuid())
polo.add_stock(4)
polo.set_price(15000)

celular = Product("Celular")
celular.set_id(generate_uuid())
celular.add_stock(10)
celular.set_price(400000)

zapatilla = Product("Zapatilla")
zapatilla.set_id(generate_uuid())
zapatilla.add_stock(2)
zapatilla.set_price(95000)

products: list[Product] = [polo, celular, zapatilla]