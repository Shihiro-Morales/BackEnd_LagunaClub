from rest_framework import routers
from rest_framework.routers import DefaultRouter

from Apps.Movimientos.Reserva.API.ReservaAPI import ReservaModelViewSet

routerReserva = DefaultRouter()

routerReserva.register('Reserva', ReservaModelViewSet, basename='Reserva')