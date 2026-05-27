from rest_framework.routers import DefaultRouter

from Apps.Catalogos.Descuento.ApiDescuento.DescuentoAPI import DescuentoModelViewSet

routerDescuento = DefaultRouter()

routerDescuento.register(prefix='Descuento', viewset=DescuentoModelViewSet, basename='Descuento')