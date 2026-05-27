from rest_framework import routers
from rest_framework.routers import DefaultRouter

from Apps.Movimientos.DayPass.API.DayPassAPI import DayPassModelViewSet

routerDayPass = DefaultRouter()

routerDayPass.register('DayPass', DayPassModelViewSet, basename='DayPass')