import psycopg2
from psycopg2 import OperationalError

def check_database_connection(host, database, user, password, port):
    try:
        conn = psycopg2.connect(host=host, database=database, user=user, password=password, port=port)
        conn.close()
        return True
    except OperationalError:
        return False

def main():
    host = input("Enter the host: ")
    database = input("Enter the database name: ")
    user = input("Enter the username: ")
    password = input("Enter the password: ")
    port = input("Enter the port number: ")

    is_successful = check_database_connection(host, database, user, password, port)
    if is_successful:
        print("Database connection successful!")
    else:
        print("Unable to connect to the database. Kindly Check the Connection Details/VPN.")

if __name__ == "__main__":
    main()
