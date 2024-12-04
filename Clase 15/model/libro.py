import json

class Libro:
    def __init__(self, autor: str, categorias: list, descripcion: str, isbn: str, numero_paginas: int, titulo: str) -> None:
        self.autor = autor
        self.categorias = categorias
        self.descripcion = descripcion
        self.isbn = isbn
        self.numero_paginas = numero_paginas
        self.titulo = titulo

    def __repr__(self) -> str:
        return f"Libro(autor={self.autor}, categorias={self.categorias}, descripcion={self.descripcion}, isbn={self.isbn}, numero_paginas={self.numero_paginas}, titulo={self.titulo})"
