from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from Seguridad.Usuario.models import Usuario


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Las contraseñas no coinciden."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')

        usuario = Usuario(

            username=validated_data['username'],

            email=validated_data['email'],

            first_name=validated_data['first_name'],

            last_name=validated_data['last_name'],

            tipo_usuario='turista'
        )

        usuario.set_password(
            validated_data['password']
        )

        usuario.save()

        return usuario

