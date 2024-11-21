from abc import ABC, abstractmethod

class Connection(ABC):
    def __init__(self, host: str, user: str, password: str, database: str) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    @abstractmethod
    def execute(self, sql: str):
        pass

    @abstractmethod
    def commit(self):
        pass
    
    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def fetchall(self):
        pass

    @abstractmethod
    def fetchone(self):
        pass