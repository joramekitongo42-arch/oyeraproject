from django.db import models
from django.core.validators import MinValueValidator
import accounts
from accounts.models import Customer


class ServiceRecord(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='service_records',
        null=True,
        blank=True,
    )
    date = models.DateField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    quantity_parts = models.IntegerField()
    parts_details = models.TextField()
    technician = models.CharField(max_length=100)


class WheelService(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='wheel_services',
        null=True,
        blank=True,
    )
    service_type = models.CharField(
        max_length=20,
        choices=[
            ('alignment', 'Wheel Alignment'),
            ('balancing', 'Wheel Balancing'),
            ('both', 'Both'),
        ],
    )
    date = models.DateField()
    technician = models.CharField(max_length=100)
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )


class PartSale(models.Model):
    customer = models.ForeignKey(
        accounts.models.Customer,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    part_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    technician = models.CharField(max_length=100)
