from django.db import models

from Seguridad.Usuario.models import Usuario


# Create your models here.
class DayPass(models.Model):

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    fecha = models.DateField()

    cantidad_personas = models.IntegerField()

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    activo = models.BooleanField(default=True)

    creado = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.usuario} - {self.fecha}"