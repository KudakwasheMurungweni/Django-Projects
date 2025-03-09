# trips/views.py
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Trip  # Only import Trip from current app
from bookings.models import Booking  # Import Booking from bookings app
from .serializers import TripSerializer
from bookings.serializers import BookingSerializer

class DashboardView(APIView):
    """
    Provides dashboard data for authenticated users
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        profile = request.user.profile
        data = {
            'upcoming_trips': self.get_upcoming_trips(profile),
            'recent_bookings': self.get_recent_bookings(profile),
            'available_trips': self.get_available_trips(profile)
        }
        return Response(data)
    
    def get_upcoming_trips(self, profile):
        trips = Trip.objects.filter(
            user=profile,
            start_date__gte=timezone.now()
        ).prefetch_related('destinations')
        return TripSerializer(trips, many=True, context={'request': self.request}).data
    
    def get_recent_bookings(self, profile):
        bookings = Booking.objects.filter(user=profile).order_by('-created_at')[:5]
        return BookingSerializer(bookings, many=True, context={'request': self.request}).data
    
    def get_available_trips(self, profile):
        # Trips not belonging to the user and not booked by them
        trips = Trip.objects.exclude(user=profile).exclude(
            bookings__user=profile
        ).distinct().prefetch_related('destinations')
        return TripSerializer(trips, many=True, context={'request': self.request}).data

class TripViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trips to be viewed or edited
    """
    queryset = Trip.objects.prefetch_related('destinations')
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Only show trips belonging to the current user"""
        return self.queryset.filter(user=self.request.user.profile)
    
    def perform_create(self, serializer):
        """Automatically associate trip with current user"""
        serializer.save(user=self.request.user.profile)
    
    def get_serializer_context(self):
        """Pass request context to serializer"""
        return {'request': self.request}