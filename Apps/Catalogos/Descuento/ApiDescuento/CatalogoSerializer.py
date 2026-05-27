from rest_framework.serializers import ModelSerializer

from Apps.Catalogos.Descuento.models import Descuento


class DescuentoSerializer(ModelSerializer):
    class Meta:
        model = Descuento
        fields = '__all__'