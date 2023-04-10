from django.db import models

# Create your models here.

class Propietarios(models.Model):
    lote = models.IntegerField(max_length= 3, unique= True)
    apellido = models.CharField(max_length= 40)
    antiguedad = models.IntegerField(max_length= 3)
    integrantes = models.IntegerField(max_length= 2)
    mascotas = models.IntegerField(max_length= 3)
        
class Torneo(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=40)
    DNI = models.IntegerField(max_length=8)
    

class Visitantes(models.Model):
    DNI = models.IntegerField(max_length= 8)
    Patente = models.CharField(max_length= 8)
    lote = models.IntegerField(max_length= 3)
