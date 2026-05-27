from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status

from Seguridad.Usuario.API.UsarioSerializer import UserCreateSerializer


class UserCreateView(APIView):
    @swagger_auto_schema(request_body=UserCreateSerializer)
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)

        #Se validan los datos
        if serializer.is_valid():
            serializer.save() #Creamos los usuarios
            return Response({"Mensaje": "Se a creado el usuario"}, status=status.HTTP_201_CREATED)
        #Si hay error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)