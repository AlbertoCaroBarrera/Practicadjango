
# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class Animals(models.Model):
    Cuidador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=200)
    Tipo = models.CharField(max_length=200)

    def __str__(self):
            return self.Nombre
    
class Protectora(models.Model):
    Nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    Fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
            return self.Nombre
    
class Colaborador(models.Model):
    Nombre = models.CharField(max_length=200)
    Cargo = models.CharField(max_length=200)
    Fecha_entrada_protectora = models.DateTimeField(default=timezone.now)

    def __str__(self):
            return self.Nombre