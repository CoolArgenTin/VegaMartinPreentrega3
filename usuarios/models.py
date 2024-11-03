from django.db import models
from django.contrib.auth.models import User


class DatosExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', default='avatar/default.png', blank=True, null=True)
    bio = models.TextField(null=True)
    
    def __str__(self):
        return f"{self.user}"

    