from rest_framework import serializers

from .models import Maintenance


class MaintenanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Maintenance
        fields = [
            "id",
            "vehicle",
            "maintenance_type",
            "description",
            "cost",
            "start_date",
            "end_date",
            "status",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]

    def validate(self, attrs):
        start_date = attrs.get("start_date")
        end_date = attrs.get("end_date")
        cost = attrs.get("cost")

        # End date cannot be before start date
        if (
            start_date
            and end_date
            and end_date < start_date
        ):
            raise serializers.ValidationError(
                {
                    "end_date": (
                        "End date cannot be before start date."
                    )
                }
            )

        # Maintenance cost must not be negative
        if cost is not None and cost < 0:
            raise serializers.ValidationError(
                {
                    "cost": (
                        "Maintenance cost cannot be negative."
                    )
                }
            )

        return attrs