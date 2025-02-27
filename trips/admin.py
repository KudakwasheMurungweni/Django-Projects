from django.contrib import admin
from .models import Trip

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'start_date', 'end_date')
    search_fields = ('title', 'user__username')
    list_filter = ('start_date', 'end_date')
