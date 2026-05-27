from django.contrib import admin

from Apps.Catalogos.Habitacion.models import Habitacion


# Register your models here.
@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre','tipo','capacidad','precio','descripcion','imagen','activa']