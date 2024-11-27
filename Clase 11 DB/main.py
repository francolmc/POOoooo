from infraestructure.mysqlconnection import MySQLConnection
from infraestructure.client_repository import ClientRepository
from credentials_db import user, password, database, host
from models.client import Client


conn = MySQLConnection(host, user, password, database)
client_repository = ClientRepository(conn)

while True:
    print("MENU MANTENEDOR")
    print("1. Mostrar todos los clientes")
    print("2. Agregar un cliente")
    print("3. Editar un cliente")
    print("4. Eliminar un cliente")
    print("5. Salir")
    option = input("Ingrese su opcion: ")
    if(option == "1"):
        print("id \t\t nombre \t\t email")
        clients = client_repository.get_all_client()
        for client in clients:
            print(f"{client.get_id()} \t\t {client.get_name()} \t\t {client.get_email()}")
    if(option == "2"):
        name = input("Ingrese el nombre del cliente: ")
        email = input("Ingrese el email del cliente: ")
        client = Client()
        client.set_name(name)
        client.set_email(email)
        client_repository.create_client(client)
        print("Cliente registrado exitosamente.")
    if(option == "3"):
        id = input("Ingrese el id del cliente: ")
        name = input("Ingrese el nombre del cliente: ")
        email = input("Ingrese el email del cliente: ")
        client = Client()
        client.set_id(id)
        client.set_name(name)
        client.set_email(email)
        client_repository.update_client(client)
        print("El cliente fue modificado exitosamente.")
    if (option == "4"):
        id = input("Ingrese el id del cliente: ")
        client_repository.delete_client(id)
        print("El cliente fue eliminado exitosamente.")
    if(option == "5"):
        break