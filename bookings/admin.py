# bookings/admin.py
from django.contrib import admin
from .models import Booking  # This is now safe

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'trip', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__user__username', 'trip__title')

admin.site.register(Booking, BookingAdmin)