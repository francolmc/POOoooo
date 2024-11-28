import requests

print("Bienvenido a la API de Rick and Morty")
print("Lista de personajes")
response_characters = requests.get("https://rickandmortyapi.com/api/character")

for character in response_characters.json()["results"]:
    print(f"ID: {character["id"]}, Nombre: {character["name"]}")

id_personaje = input("Ingrese el id del personaje: ")

# Request al endpoint de la API
response = requests.get(f"https://rickandmortyapi.com/api/character/{id_personaje}")

# Validar que la respuesta a la peticion es in OK
if response.status_code == 200:
    print("Peticion OK!!!")
    # Obtener el contenido json de la respuesta
    data = response.json()
    print("Nombre del personaje: " + data["name"])
    print("Estado: " + data["status"])
    print("Especie: " + data["species"])
    print("Genero: " + data["gender"])
else:
    print("Error")