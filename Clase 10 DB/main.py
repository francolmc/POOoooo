import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="masterdba",
    database="clase_10"
)

cursor = connection.cursor()

# INSERT
# sql = "INSERT INTO users (name) VALUES ('Franco')"
# cursor.execute(sql)
# connection.commit()

sql = "SELECT * FROM users"
cursor.execute(sql)
result = cursor.fetchmany()
print(result)

connection.close()