# bookings/models.py
from django.db import models
from users.models import Profile  # Keep this import

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    trip = models.ForeignKey(
        'trips.Trip',  # String reference avoids circular import
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.user.username} - {self.trip.title}'

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['created_at']),
        ]