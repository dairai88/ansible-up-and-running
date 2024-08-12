"""connect to mysql"""
import mysql.connector
from mysql.connector import Error


def connect_to_database():
    """connect to mysql"""
    try:
        connection = mysql.connector.connect(
            host='192.168.64.3',
            user='ghost',
            password='mysupersecretpassword',
            database='ghost'
        )

        if connection.is_connected():
            print("Successfully connected to the database")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("You're connected to database:", record)

            # Perform any database operations here
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()
            for table in tables:
                print(table)
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    connect_to_database()
