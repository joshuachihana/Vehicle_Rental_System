from django.db import models

from reservations.models import Reservation


class Rental(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        RETURNED = "RETURNED", "Returned"
        OVERDUE = "OVERDUE", "Overdue"
        CANCELLED = "CANCELLED", "Cancelled"

    reservation = models.OneToOneField(
        Reservation,
        on_delete=models.PROTECT,
        related_name="rental",
    )

    actual_pickup_datetime = models.DateTimeField()

    expected_return_datetime = models.DateTimeField()

    actual_return_datetime = models.DateTimeField(
        null=True,
        blank=True,
    )

    starting_mileage = models.PositiveIntegerField()

    ending_mileage = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rental #{self.id} - {self.reservation.vehicle}"


class VehicleInspection(models.Model):

    class InspectionType(models.TextChoices):
        PICKUP = "PICKUP", "Pickup"
        RETURN = "RETURN", "Return"

    rental = models.ForeignKey(
        Rental,
        on_delete=models.PROTECT,
        related_name="inspections",
    )

    inspection_type = models.CharField(
        max_length=10,
        choices=InspectionType.choices,
    )

    mileage = models.PositiveIntegerField()

    fuel_level = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    damage_notes = models.TextField(
        blank=True,
    )

    inspected_by = models.CharField(
        max_length=100,
    )

    inspected_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return (
            f"{self.rental} - "
            f"{self.inspection_type}"
        )