from rest_framework import serializers

from .models import Rental, VehicleInspection


class RentalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rental
        fields = [
            "id",
            "reservation",
            "actual_pickup_datetime",
            "expected_return_datetime",
            "actual_return_datetime",
            "starting_mileage",
            "ending_mileage",
            "status",
            "total_amount",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]

    def validate(self, attrs):
        reservation = attrs.get("reservation")
        actual_pickup_datetime = attrs.get(
            "actual_pickup_datetime"
        )
        expected_return_datetime = attrs.get(
            "expected_return_datetime"
        )
        actual_return_datetime = attrs.get(
            "actual_return_datetime"
        )
        starting_mileage = attrs.get(
            "starting_mileage"
        )
        ending_mileage = attrs.get(
            "ending_mileage"
        )

        # --------------------------------------------
        # 1. Reservation must be confirmed
        # --------------------------------------------

        if (
            reservation
            and reservation.status != "CONFIRMED"
        ):
            raise serializers.ValidationError(
                {
                    "reservation": (
                        "Only confirmed reservations "
                        "can be converted into a rental."
                    )
                }
            )

        # --------------------------------------------
        # 2. Reservation cannot already have a rental
        # --------------------------------------------

        if reservation:
            if hasattr(reservation, "rental"):
                if not self.instance:
                    raise serializers.ValidationError(
                        {
                            "reservation": (
                                "This reservation already "
                                "has a rental."
                            )
                        }
                    )

        # --------------------------------------------
        # 3. Expected return after pickup
        # --------------------------------------------

        if (
            actual_pickup_datetime
            and expected_return_datetime
            and actual_pickup_datetime >= expected_return_datetime
        ):
            raise serializers.ValidationError(
                {
                    "expected_return_datetime": (
                        "Expected return time must be "
                        "after actual pickup time."
                    )
                }
            )

        # --------------------------------------------
        # 4. Actual return after pickup
        # --------------------------------------------

        if (
            actual_pickup_datetime
            and actual_return_datetime
            and actual_pickup_datetime >= actual_return_datetime
        ):
            raise serializers.ValidationError(
                {
                    "actual_return_datetime": (
                        "Actual return time must be "
                        "after actual pickup time."
                    )
                }
            )

        # --------------------------------------------
        # 5. Ending mileage >= starting mileage
        # --------------------------------------------

        if (
            starting_mileage is not None
            and ending_mileage is not None
            and ending_mileage < starting_mileage
        ):
            raise serializers.ValidationError(
                {
                    "ending_mileage": (
                        "Ending mileage cannot be "
                        "less than starting mileage."
                    )
                }
            )

        return attrs


class VehicleInspectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleInspection
        fields = [
            "id",
            "rental",
            "inspection_type",
            "mileage",
            "fuel_level",
            "damage_notes",
            "inspected_by",
            "inspected_at",
        ]

        read_only_fields = [
            "id",
            "inspected_at",
        ]

    def validate_fuel_level(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError(
                "Fuel level must be between 0 and 100."
            )

        return value