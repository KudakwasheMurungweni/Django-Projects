from django.contrib import admin
from .models  import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'trip', 'booking_type')
    search_fields = ('user__user__username', 'trip__title')

admin.site.register(Booking, BookingAdmin)
                    
