from django.db import models

from Apps.Movimientos.Reserva.models import Reserva


# Create your models here.
class Pago(models.Model):

    METODOS = (
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
    )

    reserva = models.OneToOneField(
        Reserva,
        on_delete=models.CASCADE
    )

    metodo_pago = models.CharField(
        max_length=20,
        choices=METODOS
    )

    monto = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    pagado = models.BooleanField(default=False)

    fecha_pago = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Pago {self.reserva}"