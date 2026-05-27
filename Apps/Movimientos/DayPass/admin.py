from django.contrib import admin

from Apps.Movimientos.DayPass.models import DayPass


# Register your models here.
@admin.register(DayPass)
class DayPassAdmin(admin.ModelAdmin):
    search_fields = ['usuario']
    list_display = ['usuario','fecha','cantidad_personas','total','activo','creado']