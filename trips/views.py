from rest_framework import viewsets
from .models import Trip
from .serializers import TripSerializer
from rest_framework.permissions import IsAuthenticated

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context