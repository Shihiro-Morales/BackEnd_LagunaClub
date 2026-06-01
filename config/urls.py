"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from Apps.Movimientos.DayPass.API.urls import routerDayPass
from Apps.Catalogos.Descuento.ApiDescuento.urls import routerDescuento
from Apps.Catalogos.Habitacion.ApiHabitacion.urls import routerHabitacion
from Apps.Movimientos.Pago.API.urls import routerPago
from Apps.Movimientos.Reserva.API.urls import routerReserva
from Apps.Catalogos.Servicio.API.urls import routerServicio
from Seguridad.Usuario.API.UsuariosApi import UserCreateView
from Seguridad.Temporal.Temporal import crear_admin

schema_view = get_schema_view(
   openapi.Info(
      title="API Ocean Beach",
      default_version='v1',
      description="Documentación API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
path(
        'admin/',
        admin.site.urls
    ),

    path(
        'api/v1/register/',
        UserCreateView.as_view(),
        name='register'
    ),

    path(
        'api/login/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),

    path(
        'api/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),

    path(
        'api/descuento/',
        include(routerDescuento.urls)
    ),

    path(
        'api/habitacion/',
        include(routerHabitacion.urls)
    ),

    path(
        'api/servicio/',
        include(routerServicio.urls)
    ),

    path(
        'api/daypass/',
        include(routerDayPass.urls)
    ),

    path(
        'api/pago/',
        include(routerPago.urls)
    ),

    path(
        'api/reserva/',
        include(routerReserva.urls)
    ),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),

    path('swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),

    path('redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),

    path('crear-admin/', crear_admin),
]
