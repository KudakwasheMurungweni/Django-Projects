from rest_framework import serializers
from .models import Trip
from destinations.models import Destination
from destinations.serializers import DestinationSerializer

class TripSerializer(serializers.ModelSerializer):
    destinations = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Destination.objects.all()
    )

    class Meta:
        model = Trip
        fields = '__all__'
