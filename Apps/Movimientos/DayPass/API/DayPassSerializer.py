from rest_framework import serializers
from Apps.Movimientos.DayPass.models import DayPass


class DayPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayPass
        fields = '__all__'