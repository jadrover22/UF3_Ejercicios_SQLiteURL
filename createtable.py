import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Crear la tabla images
cursor.execute("""
    CREATE TABLE images(
        name text primary key,
        size text,
        date date
    );
""")

# Cerrar la conexión
conn.close()