from infraestructure.connection import Connection
from models.client import Client
from typing import List

class ClientRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def get_client_by_id(self, client_id: int) -> Client:
        sql = "SELECT id, name, email FROM Client WHERE id = %s"
        self.__conn.execute(sql, (client_id))
        result = self.__conn.fetchone()
        client = Client()
        client.set_id(result[0])
        client.set_name(result[1])
        client.set_email(result[2])
        # TODO: Realizar validacion para que retorne none cuando no exista el cliente
        return client

    # TODO: insert
    def create_client(self, client: Client) -> Client:
        sql = "INSERT INTO Client (name, email) VALUES (%s, %s)"
        self.__conn.execute(sql, (
            client.get_name(), 
            client.get_email()
        ))
        # TODO: Obtener el id del cliente insertado en base de datos y asignar al objeto
        self.__conn.commit()
        return client

    # TODO: update
    def update_client(self, client: Client) -> Client:
        sql = "UPDATE Client SET name = %s, email = %s WHERE id = %s"
        self.__conn.execute(sql, (
            client.get_name(),
            client.get_email(),
            client.get_id()
        ))
        self.__conn.commit()
        return client

    # TODO: delete
    def delete_client(self, id: int) -> None:
        sql = "DELETE FROM Client WHERE id = %s"
        self.__conn.execute(sql, (id))
        self.__conn.commit()

    # TODO: Select all
    def get_all_client(self) -> List[Client]:
        sql = "SELECT id, name, email FROM Client"
        self.__conn.execute(sql)
        results = self.__conn.fetchall()
        clients = []
        for item in results:
            client = Client()
            client.set_id(item[0])
            client.set_name(item[1])
            client.set_email(item[2])
            clients.append(client)
        return clients