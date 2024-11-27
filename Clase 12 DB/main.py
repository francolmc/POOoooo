import bcrypt
import getpass

# Encriptar contraseña
# passwd = input("Ingrese su contraseña: ")
# passwd_bytes = passwd.encode("utf-8")
# salt = bcrypt.gensalt()
# hashed_password = bcrypt.hashpw(passwd_bytes, salt)
# 
# print(hashed_password.decode("utf-8"))

hashed_password = "$2b$12$..5Bupodf4dQMHJTNyyGTO/CYlFgWUtefGK5r/KipIzwtTBo9cbe2"
hashed_password = hashed_password.encode("utf-8")

password = getpass.getpass("Ingrese la contraseña: ")
plain_password = password.encode("utf-8")
if (bcrypt.checkpw(plain_password, hashed_password)):
    print("Si, ud puede acceder a la plataforma")
else:
    print("Accedo denegado.")