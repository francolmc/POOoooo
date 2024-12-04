import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las variables de entorno
DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")


print(f"DATABASE: {DATABASE}")
print(f"USER: {USER}")
print(f"PASSWORD: {PASSWORD}")
print(f"HOST: {HOST}")