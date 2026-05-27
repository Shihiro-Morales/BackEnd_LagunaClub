from django.db import models

# Create your models here.
class Descuento(models.Model):

    nombre = models.CharField(max_length=100)

    porcentaje = models.IntegerField()

    activo = models.BooleanField(default=True)

    solo_daypass = models.BooleanField(default=False)

    fecha_inicio = models.DateField()

    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre