from django.db import models

class Celular(models.Model):
    fabricante = models.CharField(max_length=10)
    modelo = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    anio = models.IntegerField()
    
    def __str__(self):
        return f"{self.modelo} {self.color} del {self.anio}"
