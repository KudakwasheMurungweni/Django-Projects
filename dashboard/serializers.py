# dashboard/serializers.py
from rest_framework import serializers
from trips.models import Trip
from bookings.models import Booking


# dashboard/serializers.py
class DashboardTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'title', 'start_date', 'end_date']  # Remove 'status'

class DashboardBookingSerializer(serializers.ModelSerializer):
    trip_title = serializers.CharField(source='trip.title')
    trip_image = serializers.SerializerMethodField()

    def get_trip_image(self, obj):
        request = self.context.get('request')
        if obj.trip.image:
            return request.build_absolute_uri(obj.trip.image.url)
        return None

    class Meta:
        model = Booking
        fields = ['id', 'status', 'created_at', 'trip_title', 'trip_image']