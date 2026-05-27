from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from Apps.Catalogos.Habitacion.ApiHabitacion.HabitacionSerializer import HabitacionSerializer
from Apps.Catalogos.Habitacion.models import Habitacion
from Apps.Utils.ResponseData import ResponseData
from permissions.custom_permission import SoloAdmin

class HabitacionModelViewSet(ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer
    permission_classes = [SoloAdmin]



    def get_permissions(self):
        # TODOS pueden ver
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]

        # SOLO admin puede modificar
        return [SoloAdmin()]

    def list(self, request):
        serializer = HabitacionSerializer(Habitacion.objects.all(), many=True)

        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se a listado correctamente",
            Record= serializer.data
        )

        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def retrieve(self, request, pk= int):
        try:
            serch = Habitacion.objects.get(pk=pk)
            serializer = HabitacionSerializer(serch)
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se ha encontrado correctamente",
                Record= serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Habitacion.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe ese descuento",
                Record=None
            )
            return Response(data, status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def create(self, request):
        serializer = HabitacionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se a creado un nuevo descuento",
            Record= serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def update(self, request, pk= int, **kwargs):
        partial = kwargs.get('partial', False)
        try:
            certific = Habitacion.objects.get(pk=pk)
            serializer = HabitacionSerializer(instance=certific, data= request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="El registro se actualizo correctamente",
                Record= serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Habitacion.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No se ha podido actualizar el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def destroy(self, request, pk: int):
        try:
            cert = Habitacion.objects.get(pk=pk)
            cert.delete()  # elimina físicamente el registro
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se ha eliminado correctamente",
                Record=None
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Habitacion.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el registro que desea eliminar",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())