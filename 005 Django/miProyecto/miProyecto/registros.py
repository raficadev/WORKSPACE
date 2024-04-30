from contabilidad_cliente import Cliente, Factura

import datetime

fecha_nacimiento = datetime.date(1980, 12, 5)

pedro = Cliente(
    nombre = "Pedro",
    apellidos = "Aguilar Ramírez",
    rfc = "AGRM-801205-111",
    fecha_nacimiento = fecha_nacimiento,
    activo = True,
)

pedro.save()