from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    fono=models.CharField(max_length=15)

class Cargo(models.Model):
    nombre=models.CharField(max_length=30)
    sueldo=models.IntegerField() 

class Ciudad(models.Model):
    nombre=models.CharField(max_length=30)

class Comuna(models.Model):
    nombre=models.CharField(max_length=30)
    ciudad=models.ForeignKey(Ciudad,on_delete=models.CASCADE)
