from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    address = models.TextField(blank=True)

    drivers_license_number = models.CharField(
        max_length=100,
        unique=True
    )

    drivers_license_expiry = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
