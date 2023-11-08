from django.db import models

# Create your models here.
class Equipos(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_ingreso = models.DateField
    numero_serie = models.IntegerField(null=True, blank=True)
    ubicacion = models.CharField
   

def __str__(self):
    return f"{self.nombre}, {self.ubicacion}"

class Especialidades(models.Model):
    nombre = models.CharField
    edificio = models.CharField
    piso = models.CharField

class Proveedores(models.Model):
    nombre = models.CharField
    telefono = models.CharField
    mail = models.CharField

    

