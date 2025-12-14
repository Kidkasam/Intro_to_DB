import mysql.connector
from mysql.connector import Error

try:
    # CONNECT TO MYSQL SERVER
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""  # put your MySQL password here
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # CREATE DATABASE (WILL NOT FAIL IF IT EXISTS)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # CLOSE CONNECTION
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
