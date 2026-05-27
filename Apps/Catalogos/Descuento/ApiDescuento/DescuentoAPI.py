from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from Apps.Catalogos.Descuento.ApiDescuento.CatalogoSerializer import DescuentoSerializer
from Apps.Catalogos.Descuento.models import Descuento
from Apps.Utils.ResponseData import ResponseData
from permissions.custom_permission import SoloAdmin


class DescuentoModelViewSet(ModelViewSet):
    queryset = Descuento.objects.all()
    serializer_class = DescuentoSerializer



    def get_permissions(self):
        # TODOS pueden ver
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]

        # SOLO admin puede modificar
        return [SoloAdmin()]

    def list(self, request):
        serializer = DescuentoSerializer(Descuento.objects.all(), many=True)

        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se a listado correctamente",
            Record= serializer.data
        )

        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def retrieve(self, request, pk= int):
        try:
            serch = Descuento.objects.get(pk=pk)
            serializer = DescuentoSerializer(serch)
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se ha encontrado correctamente",
                Record= serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Descuento.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe ese descuento",
                Record=None
            )
            return Response(data, status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def create(self, request):
        serializer = DescuentoSerializer(data=request.data)
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
            certific = Descuento.objects.get(pk=pk)
            serializer = DescuentoSerializer(instance=certific, data= request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="El registro se actualizo correctamente",
                Record= serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Descuento.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No se ha podido actualizar el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def destroy(self, request, pk: int):
        try:
            cert = Descuento.objects.get(pk=pk)
            cert.delete()  # elimina físicamente el registro
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se ha eliminado correctamente",
                Record=None
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Descuento.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el registro que desea eliminar",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())