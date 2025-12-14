import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish connection to MySQL server (no database specified yet)
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',    # Replace with your actual MySQL username
            password='your_password' # Replace with your actual MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist - no SELECT or SHOW used
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Ensure resources are closed properly
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()