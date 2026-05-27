from rest_framework import routers
from rest_framework.routers import DefaultRouter

from Apps.Catalogos.Servicio.API.ServicioAPI import ServicioModelViewSet

routerServicio = DefaultRouter()

routerServicio.register('Servicio', ServicioModelViewSet, basename='Servicio')