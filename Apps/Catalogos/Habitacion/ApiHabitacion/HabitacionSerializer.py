from rest_framework.serializers import ModelSerializer

from Apps.Catalogos.Habitacion.models import Habitacion


class HabitacionSerializer(ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'