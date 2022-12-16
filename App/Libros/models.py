import jsonfield
from django.db import models


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    sexo = models.CharField(max_length=1)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    numero_paginas = models.IntegerField()
    descripcion = models.TextField()
    portada = models.CharField(max_length=255)

    def __str__(self):
        return self.isbn

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    rol =  jsonfield.JSONField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
