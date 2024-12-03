import json

class Libro:
    def __init__(self, autor: str, categorias: list, descripcion: str, isbn: str, numero_paginas: int, titulo: str) -> None:
        self.autor = autor
        self.categorias = categorias
        self.descripcion = descripcion
        self.isbn = isbn
        self.numero_paginas = numero_paginas
        self.titulo = titulo

    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
    
    @staticmethod # Nos permite ejecutar el metodo sin la necesidad de instanciar
    def from_json(data) -> 'Libro':
        data_dict = json.loads(data)
        return Libro(**data_dict)
