from infraestructure.connection import Connection
from models.client import Client

class ClientRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def get_client_by_id(self, client_id: int) -> Client:
        # TODO: Mejorar los parametros, utilizar los parametros de execute y no concatenar. Seguridad.
        sql = f"SELECT name, email FROM Client WHERE id = {client_id}"
        self.__conn.execute(sql)
        result = self.__conn.fetchone()
        client = Client()
        client.set_email(result[1])
        client.set_name(result[0])
        return client

    # TODO: Implementar los otros metodos.