import psycopg


def conectar():
    return psycopg.connect(
        host="127.0.0.1",
        dbname="sistema_matriculas",
        user="postgres",
        password="1234",
    )
