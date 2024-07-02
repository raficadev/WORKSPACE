from django.http import HttpResponse
import datetime

# Definición de la vista:
def saludo(request):
    texto = """
    <html>
    <body>
    <h1> Hola mundo </h1>
    </body>
    </html>
    """
    return HttpResponse(texto)

# Definición de una vista para contenido dinámico:
def fecha(request):
    miFecha = datetime.datetime.now()
    
    texto2 = """
    <html>
    <body>
    <h2> Fecha y hora actual: </h2> %s
    </body>
    </html>
    """ % miFecha
    return HttpResponse(texto2)

# Definición de una vista para calcular la edad que tendremos en un año determinado:
def calcEdad(request, edadActual, year):
    periodo = year - 2024
    edadFutura = edadActual + periodo
    documento = """
    <html>
    <body>
    <h2> En el año %s tendrás %s años. </h2>
    </body>
    </html>
    """ %(year, edadFutura)
    
    return HttpResponse(documento)