# bookings/models.py (corrected version)
from django.db import models
from users.models import Profile  # Import Profile from users app
from trips.models import Trip     # Import Trip from trips app

class Booking(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    booking_type = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return f'{self.user.user.username} - {self.trip.title}'