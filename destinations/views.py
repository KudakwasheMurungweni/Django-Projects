from rest_framework import viewsets
from .models import Destination
from rest_framework.permissions import IsAuthenticated
from .serializers import DestinationSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [IsAuthenticated]
