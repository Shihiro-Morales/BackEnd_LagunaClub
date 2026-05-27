from django.contrib import admin

from Apps.Movimientos.Reserva.models import Reserva


# Register your models here.
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    search_fields = ['usuario']
    list_display = [
        'usuario',
        'habitacion',
        'descuento',
        'mostrar_servicios',
        'fecha_entrada',
        'fecha_salida',
        'personas',
        'total',
        'estado',
        'fecha_creacion'
    ]

    def mostrar_servicios(self, obj):
        return ", ".join([s.nombre for s in obj.servicios.all()])