from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from Apps.Movimientos.Reserva.models import Reserva
from Apps.Movimientos.Reserva.API.ReservaSerializer import ReservaSerializer

from Apps.Utils.ResponseData import ResponseData


class ReservaModelViewSet(ModelViewSet):

    queryset = Reserva.objects.all()

    serializer_class = ReservaSerializer

    permission_classes = [IsAuthenticated]


    # SOLO VE SUS RESERVAS
    def get_queryset(self):

        user = self.request.user

        # ADMIN VE TODO
        if user.tipo_usuario == 'admin':
            return Reserva.objects.all()

        # TURISTA SOLO LAS SUYAS
        return Reserva.objects.filter(
            usuario=user
        )


    def list(self, request):

        serializer = ReservaSerializer(
            self.get_queryset(),
            many=True
        )

        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Reservas listadas correctamente",
            Record=serializer.data
        )

        return Response(
            status=status.HTTP_200_OK,
            data=data.toResponse()
        )


    def retrieve(self, request, pk=int):

        try:

            reserva = self.get_queryset().get(pk=pk)

            serializer = ReservaSerializer(
                reserva
            )

            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Reserva encontrada correctamente",
                Record=serializer.data
            )

            return Response(
                status=status.HTTP_200_OK,
                data=data.toResponse()
            )

        except Reserva.DoesNotExist:

            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="La reserva no existe",
                Record=None
            )

            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data=data.toResponse()
            )


    def create(self, request):

        serializer = ReservaSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )


        habitacion = serializer.validated_data['habitacion']

        fecha_entrada = serializer.validated_data['fecha_entrada']

        fecha_salida = serializer.validated_data['fecha_salida']


        # VALIDAR DISPONIBILIDAD
        conflicto = Reserva.objects.filter(

            habitacion=habitacion,

            fecha_entrada__lt=fecha_salida,

            fecha_salida__gt=fecha_entrada

        ).exists()


        if conflicto:

            data = ResponseData(
                Success=False,
                Status=status.HTTP_400_BAD_REQUEST,
                Message="La habitación está ocupada en esas fechas",
                Record=None
            )

            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=data.toResponse()
            )


        serializer.save(
            usuario=request.user
        )


        data = ResponseData(
            Success=True,
            Status=status.HTTP_201_CREATED,
            Message="Reserva creada correctamente",
            Record=serializer.data
        )

        return Response(
            status=status.HTTP_201_CREATED,
            data=data.toResponse()
        )


    def update(self, request, pk=int, **kwargs):

        partial = kwargs.get(
            'partial',
            False
        )

        try:

            reserva = self.get_queryset().get(
                pk=pk
            )

            serializer = ReservaSerializer(
                instance=reserva,
                data=request.data,
                partial=partial
            )

            serializer.is_valid(
                raise_exception=True
            )

            serializer.save()

            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Reserva actualizada correctamente",
                Record=serializer.data
            )

            return Response(
                status=status.HTTP_200_OK,
                data=data.toResponse()
            )

        except Reserva.DoesNotExist:

            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No se pudo actualizar la reserva",
                Record=None
            )

            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data=data.toResponse()
            )


    def destroy(self, request, pk=int):

        try:

            reserva = self.get_queryset().get(
                pk=pk
            )

            reserva.delete()

            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Reserva eliminada correctamente",
                Record=None
            )

            return Response(
                status=status.HTTP_200_OK,
                data=data.toResponse()
            )

        except Reserva.DoesNotExist:

            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="La reserva no existe",
                Record=None
            )

            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data=data.toResponse()
            )