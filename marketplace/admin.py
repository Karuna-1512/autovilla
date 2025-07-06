from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('title', 'vehicle_type', 'brand', 'model_name', 'price', 'fuel_type', 'mileage')
    list_filter = ('vehicle_type', 'fuel_type')
    search_fields = ('title', 'brand', 'model_name')

