from entities.shopping_cart import ShoppingCart
from entities.client import Client
from entities.status import Status
from entities.shipping import Shipping
from entities.pay import Pay
from utils.seeder import products
from utils.uuid_code import generate_uuid

# carrito = ShoppingCart()
# carrito.set_id(1)
# carrito.add_product(zapatilla, 1)
# carrito.add_product(polo, 2)

# print(carrito.get_total())

# carrito.show_detail()

def app():
    print("Bienvenido a la tienda")
    name = input("Ingrese su nombre: ")
    email = input("Ingrese su email: ")
    try:
        client = Client(name)
        client.set_id(generate_uuid())
        client.set_email(email)
    except ValueError as e:
        print(e)
        return

    shoppingCart: ShoppingCart = client.create_shopping_cart()
    
    while True:
        try:
            print("\n")
            print("1. Agregar producto al carrito")
            print("2. Eliminar producto del carrito")
            print("3. Ver carrito")
            print("4. Finalizar compra")
            print("5. Salir")
            option = input("Ingrese una opción: ")

            if option == "1":
                print("\n")
                print("Productos disponibles:")
                index = 1
                for product in products:
                    print(f"{index}. {product.name} - ${product.get_price()} - Stock: {product.get_stock()}")
                    index = index + 1
                print(f"{index}. Cancelar")

                product_index = int(input("Ingrese el índice del producto que desea agregar al carrito: "))
                if (product_index == index):
                    print("No se agregó ningún producto al carrito")
                else:
                    product = products[product_index - 1]
                    quantity = int(input("Ingrese la cantidad que desea agregar: "))

                    shoppingCart.add_product(product, quantity)
            elif option == "2":
                print("\n")
                shoppingCart.show_detail()
                product_index = int(input("Ingrese el índice del producto que desea eliminar del carrito: "))
                shoppingCart.remove_product(product_index - 1)
            elif option == "3":
                print("\n")
                shoppingCart.show_detail()
            elif option == "4":
                print("\n")
                print("Total a pagar: ${}".format(shoppingCart.get_total()))
                shipping = Shipping()
                shipping.set_id(generate_uuid())
                shipping.set_shopping_cart(shoppingCart)
                shipping.address = input("Ingrese la dirección de entrega: ")
                shipping.set_status(Status.PREPARACION)
                shipping.set_shipping_date(input("Ingrese la fecha de envío: "))
                shipping.set_delivery_date(input("Ingrese la fecha de entrega: "))
                pay = Pay()
                pay.set_id(generate_uuid())
                pay.get_shopping_cart(shoppingCart)
                pay.set_payment_date(input("Ingrese la fecha de pago: "))
                print("Compra realizada exitosamente")
                break
            elif option == "5":
                print("\n")
                print("Saliendo...")
                return
        except ValueError as e:
            print(e)


app()