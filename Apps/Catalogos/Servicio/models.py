from django.db import models

# Create your models here.
class Servicio(models.Model):

    nombre = models.CharField(max_length=100)

    descripcion = models.TextField()

    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    imagen = models.ImageField(
        upload_to='Media/Actividades/',
        blank=True,
        null=True
    )

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre