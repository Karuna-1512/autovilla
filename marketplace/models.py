from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('car', 'Car'),
        ('bike', 'Bike'),
    ]
    FUEL_TYPES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicles')
    title = models.CharField(max_length=100, default='Unknown Vehicle')
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    brand = models.CharField(max_length=100, default='Unknown Brand')
    model_name = models.CharField(max_length=100, default='Unknown Model')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPES, default='Petrol')
    image = models.ImageField(upload_to='vehicles/', blank=True, null=True, default='vehicles/default.jpg')
    mileage = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.brand} {self.model_name} ({self.vehicle_type})"
