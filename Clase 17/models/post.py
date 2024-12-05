import json

class Post:
    def __init__(self, title: str, body: str, userId: str, id: int = -1) -> None:
        self.__id = id
        self.title = title
        self.body = body
        self.userId = userId
    
    def get_id(self) -> int:
        return self.__id
    
    def set_id(self, id: int):
        self.__id = id

    def to_json(self):
        return {
            "title": self.title,
            "body": self.body,
            "userId": self.userId,
            "id": self.__id
        }
    
    @staticmethod # Nos permite ejecutar el metodo sin la necesidad de instanciar
    def from_json(data) -> 'Post':
        data_dict = json.loads(data)
        return Post(**data_dict)