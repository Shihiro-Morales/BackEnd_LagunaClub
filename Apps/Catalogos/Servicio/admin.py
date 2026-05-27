from django.contrib import admin

from Apps.Catalogos.Servicio.models import Servicio


# Register your models here.
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre','descripcion','precio','imagen','activo']