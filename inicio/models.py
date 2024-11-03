from django.db import models

class Celular(models.Model):
    fabricante = models.CharField(max_length=10)
    modelo = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    anio = models.IntegerField()
    imagen = models.ImageField(default='celu_img/default.jpg', upload_to='celu_img', blank=True, null=True)
    
    def __str__(self):
        return f"{self.modelo.capitalize()} {self.color.lower()}. Modelo {self.anio}"

