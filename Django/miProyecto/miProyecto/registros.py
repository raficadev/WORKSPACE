from contabilidad_cliente import Cliente, Factura

import datetime


fecha_nacimiento = datetime.date(1980, 12, 5)

pedro = Cliente.objects.create(
    nombre = "Pedro",
    apellidos = "Aguilar Ramírez",
    rfc = "AGRM-801205-111",
    fecha_nacimiento = fecha_nacimiento,
    activo = True,
    )

factura = Factura.objects.create(
    cliente = pedro,
    importe = 5690.12,
    pagada = False
    )


clientes = Cliente.objects.all()
for cliente in clientes:
    print(f"Nombre: {cliente.nombre}, Apellidos: {cliente.apellidos}")
    
facturas = Factura.objects.all()
for factura in facturas:
    print(f"Pagada: {factura.pagada}, Importe: {factura.importe}, RFC Cliente: {factura.cliente.rfc}")