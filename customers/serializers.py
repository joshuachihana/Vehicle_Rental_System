from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone",
            "email",
            "address",
            "drivers_license_number",
            "drivers_license_expiry",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]