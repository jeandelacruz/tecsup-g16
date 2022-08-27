from psycopg2 import connect

connection = connect(
    user='postgres',
    password='mysql',
    host='localhost',
    port=5432,
    database='tecsup'
)

cursor = connection.cursor()

# cursor.execute("SELECT version();")
# fetchone -> Usar cuando la consulta traiga una fila
# fetchall -> Usar cuando la consulta traiga mas de una fila

# record = cursor.fetchone()
# record = cursor.fetchall()
# print(record)

# Transaccionalidad Insert, Update, Delete
try:
    cursor.execute("INSERT INTO area (name) VALUES ('Mineria');")
    connection.commit()
except Exception as e:
    connection.rollback()
    print(f'Ocurrio un error -> {e}')

# Obligatorio cerrar la sesión y la conexión
cursor.close()
connection.close()
