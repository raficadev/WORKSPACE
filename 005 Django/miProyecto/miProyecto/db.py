from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length = 64)
    apellidos = models.CharField(max_length = 64)
    rfc = models.CharField(max_length = 15, unique = True)
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default = True)