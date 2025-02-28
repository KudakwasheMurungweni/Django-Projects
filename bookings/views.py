# bookings/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']  # Ensure POST is allowed

    def get_queryset(self):
        # You can restrict the queryset based on the logged-in user
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Ensure the logged-in user is automatically assigned to the booking
        serializer.save(user=self.request.user)
