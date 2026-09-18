from django.db import models


class VehicleType(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    seats = models.PositiveIntegerField()

    transmission = models.CharField(
        max_length=20,
        choices=[
            ("MANUAL", "Manual"),
            ("AUTOMATIC", "Automatic"),
        ],
    )

    fuel_type = models.CharField(
        max_length=20,
        choices=[
            ("PETROL", "Petrol"),
            ("DIESEL", "Diesel"),
            ("ELECTRIC", "Electric"),
            ("HYBRID", "Hybrid"),
        ],
    )

    daily_rate = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    def __str__(self):
        return self.name


class Vehicle(models.Model):

    class Status(models.TextChoices):
        AVAILABLE = "AVAILABLE", "Available"
        RESERVED = "RESERVED", "Reserved"
        RENTED = "RENTED", "Rented"
        MAINTENANCE = "MAINTENANCE", "Maintenance"
        UNAVAILABLE = "UNAVAILABLE", "Unavailable"

    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.PROTECT,
        related_name="vehicles",
    )

    registration_number = models.CharField(
        max_length=20,
        unique=True,
    )

    make = models.CharField(max_length=100)

    model = models.CharField(max_length=100)

    year = models.PositiveIntegerField()

    color = models.CharField(max_length=50)

    current_mileage = models.PositiveIntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.make} {self.model} - {self.registration_number}"





