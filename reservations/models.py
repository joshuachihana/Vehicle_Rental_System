from django.db import models

from customers.models import Customer
from vehicles.models import Vehicle
from locations.models import Location


class Reservation(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        CONFIRMED = "CONFIRMED", "Confirmed"
        CANCELLED = "CANCELLED", "Cancelled"
        EXPIRED = "EXPIRED", "Expired"
        COMPLETED = "COMPLETED", "Completed"

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name="reservations",
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        related_name="reservations",
    )

    pickup_location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        related_name="pickup_reservations",
    )

    return_location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        related_name="return_reservations",
    )

    pickup_datetime = models.DateTimeField()

    return_datetime = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.customer} - "
            f"{self.vehicle} - "
            f"{self.pickup_datetime}"
        )