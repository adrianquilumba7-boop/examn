from django.db import models

# Create your models here.
from django.db import models

class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    director = models.CharField(max_length=150)
    año_lanzamiento = models.IntegerField()
    sinopsis = models.TextField()

    def __str__(self):
        return self.nombre
