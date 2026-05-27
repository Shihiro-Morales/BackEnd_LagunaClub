from django.contrib import admin

from Apps.Catalogos.Descuento.models import Descuento


# Register your models here.
@admin.register(Descuento)
class DescuentoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre', 'porcentaje','activo','solo_daypass','fecha_inicio','fecha_fin']