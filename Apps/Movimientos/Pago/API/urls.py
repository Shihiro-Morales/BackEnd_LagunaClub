from rest_framework import routers
from rest_framework.routers import DefaultRouter

from Apps.Movimientos.Pago.API.PagoAPI import PagoModelViewSet

routerPago = DefaultRouter()

routerPago.register('Pago', PagoModelViewSet, basename='Pago')