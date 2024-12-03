import json

class Libro:
    def __init__(self, autor: str, categorias: list, descripcion: str, isbn: str, nro_paginas: int, titulo: str) -> None:
        self.autor = autor
        self.categorias = categorias
        self.descripcion = descripcion
        self.isbn = isbn
        self.nro_paginas = nro_paginas
        self.titulo = titulo

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
    
    