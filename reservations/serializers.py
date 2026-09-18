from rest_framework import serializers

from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = [
            "id",
            "reference",
            "customer",
            "vehicle",
            "pickup_location",
            "return_location",
            "pickup_datetime",
            "return_datetime",
            "status",
            "total_amount",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]

    def validate(self, attrs):
        pickup_datetime = attrs.get("pickup_datetime")
        return_datetime = attrs.get("return_datetime")
        vehicle = attrs.get("vehicle")

        # -------------------------------------------------
        # 1. Pickup must be before return
        # -------------------------------------------------

        if (
            pickup_datetime
            and return_datetime
            and pickup_datetime >= return_datetime
        ):
            raise serializers.ValidationError(
                {
                    "return_datetime": (
                        "Return time must be after pickup time."
                    )
                }
            )

        # -------------------------------------------------
        # 2. Vehicle must be available
        # -------------------------------------------------

        if vehicle and vehicle.status != "AVAILABLE":
            raise serializers.ValidationError(
                {
                    "vehicle": (
                        "This vehicle is not currently available."
                    )
                }
            )

        # -------------------------------------------------
        # 3. Check for overlapping reservations
        # -------------------------------------------------

        if vehicle and pickup_datetime and return_datetime:

            overlapping_reservations = Reservation.objects.filter(
                vehicle=vehicle,
                pickup_datetime__lt=return_datetime,
                return_datetime__gt=pickup_datetime,
                status__in=[
                    Reservation.Status.PENDING,
                    Reservation.Status.CONFIRMED,
                ],
            )

            # Exclude current reservation during PATCH/PUT
            if self.instance:
                overlapping_reservations = (
                    overlapping_reservations.exclude(
                        pk=self.instance.pk
                    )
                )

            if overlapping_reservations.exists():
                raise serializers.ValidationError(
                    {
                        "vehicle": (
                            "This vehicle is already reserved "
                            "during the selected period."
                        )
                    }
                )

        return attrs