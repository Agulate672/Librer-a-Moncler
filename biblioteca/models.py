from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    nacionalidad = models.CharField(max_length=30)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    genero = models.CharField(max_length=100)
    cantidad_paginas = models.IntegerField()
    disponible = models.BooleanField(default=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo





