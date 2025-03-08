from rest_framework import serializers
from .models import Trip
from destinations.models import Destination
from destinations.serializers import DestinationSerializer

class TripSerializer(serializers.ModelSerializer):
    destinations = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Destination.objects.all()
    )
    image = serializers.SerializerMethodField()
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
        return None
    
    class Meta:
        model = Trip
        fields = '__all__'