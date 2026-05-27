from django.contrib import admin

from Apps.Movimientos.Pago.models import Pago


# Register your models here.
@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    search_fields = ['reserva']
    list_display = ['reserva','metodo_pago','monto','pagado','fecha_pago']