import psycopg2
from psycopg2 import OperationalError

def get_connection():
    try:
        return psycopg2.connect(
            host="localhost", database="sistema_matriculas", user="postgres", password="1234"
        )
    except OperationalError as e:
        print(f"\nErro de conexão com o banco")
        return None