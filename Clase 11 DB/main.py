from infraestructure.mysqlconnection import MySQLConnection
from infraestructure.client_repository import ClientRepository
from credentials_db import user, password, database, host


conn = MySQLConnection(host, user, password, database)
client_repository = ClientRepository(conn)
client = client_repository.get_client_by_id(1)
print(client.get_email())