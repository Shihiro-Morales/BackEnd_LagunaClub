from rest_framework import routers
from rest_framework.routers import DefaultRouter

from Apps.Catalogos.Habitacion.ApiHabitacion.HabitacionAPI import HabitacionModelViewSet

routerHabitacion = DefaultRouter()

routerHabitacion.register(prefix='Habitacion', viewset=HabitacionModelViewSet, basename='Habitacion')