from django.db import models

from vehicles.models import Vehicle


class Maintenance(models.Model):

    class Status(models.TextChoices):
        SCHEDULED = "SCHEDULED", "Scheduled"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        related_name="maintenance_records",
    )

    maintenance_type = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
    )

    cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    start_date = models.DateField()

    end_date = models.DateField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.SCHEDULED,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.vehicle} - {self.maintenance_type}"