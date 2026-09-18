from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Rental, VehicleInspection
from .serializers import (
    RentalSerializer,
    VehicleInspectionSerializer,
)


class RentalListCreateAPIView(APIView):

    def get(self, request):
        rentals = Rental.objects.all()

        serializer = RentalSerializer(
            rentals,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = RentalSerializer(
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


class RentalDetailAPIView(APIView):

    def get(self, request, pk):
        rental = get_object_or_404(
            Rental,
            pk=pk
        )

        serializer = RentalSerializer(rental)

        return Response(serializer.data)

    def put(self, request, pk):
        rental = get_object_or_404(
            Rental,
            pk=pk
        )

        serializer = RentalSerializer(
            rental,
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
        rental = get_object_or_404(
            Rental,
            pk=pk
        )

        serializer = RentalSerializer(
            rental,
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
        rental = get_object_or_404(
            Rental,
            pk=pk
        )

        rental.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class VehicleInspectionListCreateAPIView(APIView):

    def get(self, request):
        inspections = VehicleInspection.objects.all()

        serializer = VehicleInspectionSerializer(
            inspections,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = VehicleInspectionSerializer(
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


class VehicleInspectionDetailAPIView(APIView):

    def get(self, request, pk):
        inspection = get_object_or_404(
            VehicleInspection,
            pk=pk
        )

        serializer = VehicleInspectionSerializer(
            inspection
        )

        return Response(serializer.data)

    def put(self, request, pk):
        inspection = get_object_or_404(
            VehicleInspection,
            pk=pk
        )

        serializer = VehicleInspectionSerializer(
            inspection,
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
        inspection = get_object_or_404(
            VehicleInspection,
            pk=pk
        )

        serializer = VehicleInspectionSerializer(
            inspection,
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
        inspection = get_object_or_404(
            VehicleInspection,
            pk=pk
        )

        inspection.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
