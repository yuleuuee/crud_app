import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'rabhav9861'
)
    

# prepare a cursor object
cursorObject = dataBase.cursor ()

# Create a database

cursorObject.execute("CREATE DATABASE IF NOT EXISTS crud_app_db")
print("Database created!")