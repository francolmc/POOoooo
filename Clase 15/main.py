import requests
import pickle
from model.libro import Libro

# Serealizar la instancia a JSON
libro = Libro("Hans Topo", ["psicologia", "autoayuda"], "Explica como comer una naranja en este mundo tan cruel.", "123-123", 123, "Como comer una naranja sin poner caras")
libro_deserializado = pickle.dumps(libro)
print(libro_deserializado)
print(libro.__repr__())
# Deserializacion de un JSON a una instancia
response = requests.get("https://poo.nsideas.cl/api/libros/978-3-16-148410-0")
if response.status_code == 200:
    data = response.json()
    libro2 = pickle.loads(data)
    print(libro2)