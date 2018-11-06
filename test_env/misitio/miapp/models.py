from django.db import models
from django.utils import timezone

# Create your models here.
class Vehiculo(models.Model):
    autor= models.ForeignKey('auth.User',on_delete=models.CASCADE)
    marca = models.CharField(max_length=30)
    modelo =models.CharField(max_length=30)
    anio=models.CharField(max_length=5)
    color=models.CharField(max_length=30)
    n_puertas=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=30)
    fecha_publicacion=models.DateTimeField(blank=True, null=True)
    precio = models.CharField(max_length=30)

    def publish(self):         
         self.fecha_publicacion = timezone.now()         
         self.save()
 
    def __str__(self):         
        return self.marca 