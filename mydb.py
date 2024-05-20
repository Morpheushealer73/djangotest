import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin1234',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE testdjangodb")

print("Database created YAY")