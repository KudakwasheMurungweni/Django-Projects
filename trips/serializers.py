from rest_framework import serializers
from .models import Trip
from destinations.models import Destination
from destinations.serializers import DestinationSerializer

# trips/serializers.py

# trips/serializers.py
# trips/serializers.py
from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(
        choices=[
            ('planning', 'Planning'),
            ('upcoming', 'Upcoming'),
            ('ongoing', 'Ongoing'),
            ('completed', 'Completed')
        ]
    )
    
    class Meta:
        model = Trip
        fields = '__all__'