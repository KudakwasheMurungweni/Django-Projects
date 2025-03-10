# bookings/serializers.py
from rest_framework import serializers
from .models import Booking
from trips.serializers import TripSerializer

class BookingSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Booking.STATUS_CHOICES)
    
    class Meta:
        model = Booking
        fields = [
            'id', 'status', 'trip', 'details',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def to_representation(self, instance):
        # Serialize the trip using TripSerializer when reading
        representation = super().to_representation(instance)
        representation['trip'] = TripSerializer(instance.trip).data
        return representation