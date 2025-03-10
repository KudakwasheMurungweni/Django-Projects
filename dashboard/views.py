from django.shortcuts import render

# dashboard/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from trips.models import Trip
from bookings.models import Booking
from .serializers import DashboardTripSerializer, DashboardBookingSerializer

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        profile = request.user.profile
        context = {'request': request}
        
        data = {
            'user': self.get_user_data(profile),
            'upcoming_trips': self.get_upcoming_trips(profile, context),
            'recent_bookings': self.get_recent_bookings(profile, context),
            'available_trips': self.get_available_trips(profile, context)
        }
        return Response(data)

    def get_user_data(self, profile):
        return {
            'username': profile.user.username,
            'email': profile.user.email,
            'phone': profile.phone,
            'bio': profile.bio
        }

    def get_upcoming_trips(self, profile, context):
        trips = Trip.objects.filter(
            user=profile,
            start_date__gte=timezone.now()
        ).prefetch_related('destinations')[:5]
        return DashboardTripSerializer(trips, many=True, context=context).data

    def get_recent_bookings(self, profile, context):
        bookings = Booking.objects.filter(
            user=profile
        ).order_by('-created_at')[:5]
        return DashboardBookingSerializer(bookings, many=True, context=context).data

    def get_available_trips(self, profile, context):
        trips = Trip.objects.exclude(user=profile).exclude(
            bookings__user=profile
        ).distinct().prefetch_related('destinations')[:10]
        return DashboardTripSerializer(trips, many=True, context=context).data
