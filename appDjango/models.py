from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_de_nacimiento = models.CharField(max_length=200)
    dni = models.IntegerField()
    def __str__(self):
      return f"{self.nombre}, {self.fecha_de_nacimiento}, {self.dni}"
    
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    animal = models.CharField(max_length=50)
    def __str__(self):
      return f"{self.nombre}, {self.edad}, {self.animal}"
    
class Vehiculo(models.Model):
    tipo = models.CharField(max_length=50)
    antiguedad = models.IntegerField()
    marca = models.CharField(max_length=50)