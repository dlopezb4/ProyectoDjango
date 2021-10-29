from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre =models.CharField(max_length=50)
    apellido =models.CharField(max_length=50)
    direccion =models.CharField(max_length=200)
    nacimiento =models.DateField()
    creacion =models.DateField(auto_created=True)
    actualizacion  =models.DateField(auto_created=True)
     
    def __str__(self):
        return  '%s %s' % (self.nombre, self.apellido) 


class TipoCliente(models.Model):
    tipo =models.CharField(max_length=10)
    creacion =models.DateField(auto_created=True)
    actualizacion  =models.DateField(auto_created=True)

    def __str__(self):
        return  '%s' % (self.tipo) 


class Estudiante(models.Model):
    nombre =models.CharField(max_length=50)
    apellido =models.CharField(max_length=50)
    direccion =models.CharField(max_length=100)
    def __str__(self):
        return  '%s %s' % (self.nombre, self.apellido) 

class Administradores(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)

    def __str__(self) -> str:
        return '%s %s' %(self.nombre, self.apellido)
        