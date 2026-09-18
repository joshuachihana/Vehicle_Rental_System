from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)

    address = models.TextField()

    city = models.CharField(max_length=100)

    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name