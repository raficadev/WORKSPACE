import sqlite3

miConexion = sqlite3.connect("/Users/rafel/WORKSPACE/004 BD/GestionStock2.db")

miCursor = miConexion.cursor()

"""
miCursor.execute('''
                 create table Productos(
                 ID integer primary key autoincrement,
                 Artículo varchar(9999) unique,
                 Precio integer,
                 Sección varchar(9999))
                 ''')

Productos = [
    ("Bañador", 22, "Verano"),
    ("Toalla", 15, "Verano"),
    ("Manguera", 40, "Jardín"),
    ("Cubo", 3, "Jardín"),
    ("Toalla de playa", 30, "Verano")
]

miCursor.executemany("insert into Productos values (NULL, ?, ?, ?)", Productos)
"""
"""
miCursor.execute("SELECT * from Productos where Sección = 'Verano'")

Productos = miCursor.fetchall()

print(Productos)
"""

#miCursor.execute("Update Productos set Precio = 35 where Artículo = 'Manguera'")

miCursor.execute("Delete from Productos where ID = 1")

miConexion.commit()

miConexion.close()