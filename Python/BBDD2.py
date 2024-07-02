import sqlite3

miConexion = sqlite3.connect("/Users/rafel/WORKSPACE/004 BD/GestionStock.db")

miCursor = miConexion.cursor()

"""
miCursor.execute('''
                 create table Productos(
                 Código varchar(999999) primary key,
                 Artículo varchar(999999),
                 Precio integer,
                 Sección varchar(999999))
                 ''')

Productos = [
    ("CO01", "Bañador", 22, "Verano"),
    ("CO02", "Toalla", 15, "Verano"),
    ("CO03", "Manguera", 40, "Jardín"),
    ("CO04", "Cubo", 3, "Jardín")
]

miCursor.executemany("insert into Productos values (?, ?, ?, ?)", Productos)
"""

miCursor.execute("insert into Productos values ('CO05', 'Raqueta', 90, 'Deportes')")

miConexion.commit()

miConexion.close()