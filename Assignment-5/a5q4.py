import mysql.connector
from mysql.connector import Error

connection = None
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="deeznuts",
        database="eurekadb"
    )
    if connection.is_connected():
        print("Connected to MySQL database")
except Error as e:
    print(f"Error: {e}")
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")