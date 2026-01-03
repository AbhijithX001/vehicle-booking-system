from django.contrib import admin
from .models import Vehicle, Booking

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'year', 'price_per_day', 'fuel_type', 'is_available']
    list_filter = ['brand', 'fuel_type', 'is_available']
    search_fields = ['name', 'brand']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'vehicle', 'start_date', 'end_date', 'total_amount']
    list_filter = ['start_date', 'end_date']
    search_fields = ['customer_name', 'customer_phone']
    