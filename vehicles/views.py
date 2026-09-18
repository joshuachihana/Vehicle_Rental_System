from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Vehicle, VehicleType
from .serializers import (
    VehicleSerializer,
    VehicleTypeSerializer,
)


class VehicleTypeListCreateAPIView(APIView):

    def get(self, request):
        vehicle_types = VehicleType.objects.all()

        serializer = VehicleTypeSerializer(
            vehicle_types,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = VehicleTypeSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class VehicleTypeDetailAPIView(APIView):

    def get(self, request, pk):
        vehicle_type = get_object_or_404(
            VehicleType,
            pk=pk
        )

        serializer = VehicleTypeSerializer(vehicle_type)

        return Response(serializer.data)

    def put(self, request, pk):
        vehicle_type = get_object_or_404(
            VehicleType,
            pk=pk
        )

        serializer = VehicleTypeSerializer(
            vehicle_type,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        vehicle_type = get_object_or_404(
            VehicleType,
            pk=pk
        )

        serializer = VehicleTypeSerializer(
            vehicle_type,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        vehicle_type = get_object_or_404(
            VehicleType,
            pk=pk
        )

        vehicle_type.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class VehicleListCreateAPIView(APIView):

    def get(self, request):
        vehicles = Vehicle.objects.all()

        serializer = VehicleSerializer(
            vehicles,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = VehicleSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class VehicleDetailAPIView(APIView):

    def get(self, request, pk):
        vehicle = get_object_or_404(
            Vehicle,
            pk=pk
        )

        serializer = VehicleSerializer(vehicle)

        return Response(serializer.data)

    def put(self, request, pk):
        vehicle = get_object_or_404(
            Vehicle,
            pk=pk
        )

        serializer = VehicleSerializer(
            vehicle,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        vehicle = get_object_or_404(
            Vehicle,
            pk=pk
        )

        serializer = VehicleSerializer(
            vehicle,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        vehicle = get_object_or_404(
            Vehicle,
            pk=pk
        )

        vehicle.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )