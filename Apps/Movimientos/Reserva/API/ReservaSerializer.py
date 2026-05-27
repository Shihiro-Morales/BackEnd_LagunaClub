from rest_framework import serializers

from Apps.Movimientos.Reserva.models import Reserva


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'