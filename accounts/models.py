from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_mechanic = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='customer_profile',
    )
    vehicle_model = models.CharField(max_length=100, blank=True, null=True)
    vehicle_plate = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
