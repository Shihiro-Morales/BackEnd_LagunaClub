from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):

    TIPOS = (
        ('admin', 'Administrador'),
        ('turista', 'Turista'),
        ('local', 'Local'),
    )

    tipo_usuario = models.CharField(
        max_length=20,
        choices=TIPOS,
        default='turista'
    )

    telefono = models.CharField(
        max_length=20,
        blank=True
    )

    foto = models.ImageField(
        upload_to='Media/Usuario/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username
