from django.db import models

# Create your models here.
class Habitacion(models.Model):

    TIPOS = (
        ('master', 'Master'),
        ('familiar', 'Familiar'),
        ('dormitorio', 'Compartida'),
    )

    nombre = models.CharField(max_length=100)

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS
    )

    capacidad = models.IntegerField()

    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    descripcion = models.TextField()

    imagen = models.ImageField(
        upload_to='Media/Habitaciones/',
        blank=True,
        null=True
    )

    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre