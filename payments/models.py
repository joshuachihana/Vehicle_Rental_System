from django.db import models

from reservations.models import Reservation


class Payment(models.Model):

    class PaymentMethod(models.TextChoices):
        CASH = "CASH", "Cash"
        CARD = "CARD", "Card"
        BANK_TRANSFER = "BANK_TRANSFER", "Bank Transfer"
        AIRTEL_MONEY = "AIRTEL_MONEY", "Airtel Money"
        TNM_MPAMBA = "TNM_MPAMBA", "TNM Mpamba"

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        SUCCESSFUL = "SUCCESSFUL", "Successful"
        FAILED = "FAILED", "Failed"
        REFUNDED = "REFUNDED", "Refunded"

    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.PROTECT,
        related_name="payments",
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PaymentMethod.choices,
    )

    transaction_reference = models.CharField(
        max_length=100,
        unique=True,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    paid_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return (
            f"{self.transaction_reference} - "
            f"{self.amount}"
        )