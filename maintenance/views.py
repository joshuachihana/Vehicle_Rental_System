from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Maintenance
from .serializers import MaintenanceSerializer


class MaintenanceListCreateAPIView(APIView):

    def get(self, request):
        maintenance_records = Maintenance.objects.all()

        serializer = MaintenanceSerializer(
            maintenance_records,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = MaintenanceSerializer(
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


class MaintenanceDetailAPIView(APIView):

    def get(self, request, pk):
        maintenance = get_object_or_404(
            Maintenance,
            pk=pk
        )

        serializer = MaintenanceSerializer(
            maintenance
        )

        return Response(serializer.data)

    def put(self, request, pk):
        maintenance = get_object_or_404(
            Maintenance,
            pk=pk
        )

        serializer = MaintenanceSerializer(
            maintenance,
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
        maintenance = get_object_or_404(
            Maintenance,
            pk=pk
        )

        serializer = MaintenanceSerializer(
            maintenance,
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
        maintenance = get_object_or_404(
            Maintenance,
            pk=pk
        )

        maintenance.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )