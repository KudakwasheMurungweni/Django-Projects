from django.db import models
from users.models import Profile
from destinations.models import Destination


class Trip(models.Model):
    # Use string format for foreign key to avoid circular imports
    user = models.ForeignKey(
        'users.Profile', 
        on_delete=models.CASCADE,
        related_name='trips'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    # Use string reference for ManyToManyField
    destinations = models.ManyToManyField(
        'destinations.Destination',
        related_name='trips'
    )
    
    image = models.ImageField(
        upload_to='trip_images/',
        null=True,
        blank=True,
        help_text='Upload trip cover image'
    )
    activities = models.TextField(
        null=True,
        blank=True,
        help_text='List of planned activities (comma-separated)'
    )

    # Add automatic timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.start_date} to {self.end_date})"

    class Meta:
        ordering = ['-start_date']
        indexes = [
            models.Index(fields=['start_date', 'end_date']),
            models.Index(fields=['title'], name='title_idx'),
        ]
