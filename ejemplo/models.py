from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
   

    def __str__(self):
        return f"{self.nombre},{self.direccion},{self.numero_pasaporte},{self.id}"


 #   nombre = models.CharField(max_length=100)


class Mascota(models.Model):
    animal = models.CharField(max_length=100) 
    nombre = models.CharField(max_length=100)
    dueno = models.CharField(max_length=200)
   
    def __str__(self):
        return f"{self.animal},{self.nombre},{self.dueno},{self.id}"

class Vehiculo(models.Model):
    tipo = models.CharField(max_length=100) 
    marca = models.CharField(max_length=100)
    titular = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.tipo},{self.marca},{self.titular},{self.id}"