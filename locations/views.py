from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Location
from .serializers import LocationSerializer


class LocationListCreateAPIView(APIView):

    def get(self, request):
        locations = Location.objects.all()

        serializer = LocationSerializer(
            locations,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = LocationSerializer(
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


class LocationDetailAPIView(APIView):

    def get(self, request, pk):
        location = get_object_or_404(
            Location,
            pk=pk
        )

        serializer = LocationSerializer(location)

        return Response(serializer.data)

    def put(self, request, pk):
        location = get_object_or_404(
            Location,
            pk=pk
        )

        serializer = LocationSerializer(
            location,
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
        location = get_object_or_404(
            Location,
            pk=pk
        )

        serializer = LocationSerializer(
            location,
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
        location = get_object_or_404(
            Location,
            pk=pk
        )

        location.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )