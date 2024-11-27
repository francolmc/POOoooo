from infraestructure.connection import Connection
import pymysql

class MySQLConnection(Connection):
    def __init__(self, host: str, user: str, password: str, database: str) -> None:
        super().__init__(host, user, password, database)
        self.__connection = pymysql.connect(
            host=host,
            user=user,
            passwd=password,
            database=database
        )
        self.__cursor = self.__connection.cursor()

    def execute(self, sql: str, args: object = None):
        self.__cursor.execute(sql, args)

    def commit(self):
        
        self.__connection.commit()

    def close(self):
        self.__connection.close()

    def fetchall(self):
        return self.__cursor.fetchall()
    
    def fetchone(self):
        return self.__cursor.fetchone()
    