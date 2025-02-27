from rest_framework import viewsets
from .models import Booking
from rest_framework.permissions import IsAuthenticated
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]