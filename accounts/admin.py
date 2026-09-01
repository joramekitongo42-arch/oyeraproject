
from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    # We use 'get_phone_number' instead of 'phone_number'
    list_display = (
        'user',
        'get_phone_number',
        'vehicle_model',
        'vehicle_plate',
    )
    search_fields = ('user__username', 'vehicle_plate')

    # This method fetches the data from the related User model
    def get_phone_number(self, obj):
        return obj.user.phone_number
    
    # This sets the column header name in the admin dashboard
    get_phone_number.short_description = 'Phone Number'
    