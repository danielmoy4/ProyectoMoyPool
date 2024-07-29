from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=255)
    cantidad = models.IntegerField()

class Stock(models.Model):
    cantidad = models.IntegerField()
    nombre_producto = models.CharField(max_length=255)