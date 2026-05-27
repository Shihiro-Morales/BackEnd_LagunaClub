from django.db import models

from Apps.Catalogos.Descuento.models import Descuento
from Apps.Catalogos.Habitacion.models import Habitacion
from Apps.Catalogos.Servicio.models import Servicio
from Seguridad.Usuario.models import Usuario


# Create your models here.
class Reserva(models.Model):

    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('finalizada', 'Finalizada'),
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    habitacion = models.ForeignKey(
        Habitacion,
        on_delete=models.CASCADE
    )

    descuento = models.ForeignKey(
        Descuento,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    servicios = models.ManyToManyField(
        Servicio,
        blank=True
    )

    fecha_entrada = models.DateField()

    fecha_salida = models.DateField()

    personas = models.IntegerField()

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='pendiente'
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.usuario} - {self.habitacion}"