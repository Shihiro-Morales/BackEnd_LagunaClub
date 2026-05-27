from rest_framework import serializers

from Apps.Catalogos.Servicio.models import Servicio


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'