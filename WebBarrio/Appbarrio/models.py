from django.db import models

# Create your models here.

class Asociados(models.Model):
    apellido_familia= models.CharField(max_length= 40)
    email = models.EmailField(max_length=30)
    DNI = models.CharField(max_length = 8)
    integrantes = models.CharField(max_length=2)
    mascotas = models.CharField(max_length=4)
    def __str__(self):
        return "Ya sos parte de la familia!"
        
class Torneo(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length= 40)
    DNI = models.CharField(max_length= 8)
    def __str__(self):
        return f"Ya estas insripto {self.nombre}! En breve te enviaremos toda la información sobre el torneo a tu email!"

class Terrenos(models.Model):
    nombre = models.CharField(max_length= 20)
    apellido = models.CharField(max_length= 40)
    telefono = models.CharField(max_length= 16)
    email = models.EmailField(max_length= 40)
    def __str__(self):
        return f"{self.nombre} pronto te contactaremos para atender tu solicitud y brindarte toda la información disponibe!"
    