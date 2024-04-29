import sqlite3

miConexion = sqlite3.connect("/Users/rafel/WORKSPACE/004 BD/MiBase.db")

miCursor = miConexion.cursor()

"""
miCursor.execute("create table productos (nombre_articulo varchar(50), precio integer, seccion varchar(20))")

# miCursor.execute("insert into productos values('Balón', 15, 'deportes')")

masProductos = [

    ("Camiseta", 20, "Moda"),
    ("Lampara", 60, "Decoración"),
    ("Tornillos", 1, "Ferreteria")

]

miCursor.executemany("insert into productos values (?, ?, ?)", masProductos)
"""

miCursor.execute("Select * from productos")

misProductos = miCursor.fetchall()

# print(misProductos)

for producto in misProductos:
    print("Nombre del artículo:", producto[0], "/", "Precio:", producto[1], "€", "/", "Sección:", producto[2])

miConexion.commit()

miConexion.close()