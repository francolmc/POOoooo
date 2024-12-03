import requests
from model.libro import Libro

libro = Libro("prueba", ["prueba"], "prueba", "123-123", 123, "pruebita")
print(libro.to_json())

response = requests.get("https://poo.nsideas.cl/api/libros/978-3-16-148410-0")

if response.status_code == 200:
    data = response.json()
    print(data)