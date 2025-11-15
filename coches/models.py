
from django.db import models

class Coche(models.Model):
    modelo = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.modelo} - {self.precio}€"
