from django.db import models

# Create your models here.

class Libro(models.Model):
    id = models.AutoField(primary_key=True)    
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    editorial = models.CharField(max_length=100, verbose_name="Editorial")

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)
    INE = models.CharField(max_length=50)

class Prestamo(models.Model):
    libro =  models.ForeignKey(Libro, on_delete=models.CASCADE)
    cliente =  models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_prestamo = models.CharField(max_length=10)
    fecha_devolucion = models.CharField(max_length=10)