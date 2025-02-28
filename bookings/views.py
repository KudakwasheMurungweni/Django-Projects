# bookings/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_queryset(self):
        # Filter bookings by the logged-in user's PROFILE
        return Booking.objects.filter(user=self.request.user.profile)  # 👈 Changed

    def perform_create(self, serializer):
        # Assign the user's PROFILE (not the User instance)
        serializer.save(user=self.request.user.profile)  # 👈 Changed