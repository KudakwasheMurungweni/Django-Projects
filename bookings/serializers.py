# bookings/serializers.py
from rest_framework import serializers
from .models import Booking
from trips.serializers import TripSerializer

class BookingSerializer(serializers.ModelSerializer):
    trip = TripSerializer(read_only=True)
    status = serializers.ChoiceField(choices=Booking.STATUS_CHOICES)
    
    class Meta:
        model = Booking
        fields = [
            'id', 'status', 'trip', 'details',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']