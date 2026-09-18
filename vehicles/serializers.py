from rest_framework import serializers

from .models import Vehicle, VehicleType


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = [
            "id",
            "name",
            "description",
            "seats",
            "transmission",
            "fuel_type",
            "daily_rate",
        ]

        read_only_fields = [
            "id",
        ]


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            "id",
            "vehicle_type",
            "registration_number",
            "make",
            "model",
            "year",
            "color",
            "current_mileage",
            "status",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]