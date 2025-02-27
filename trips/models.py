from django.db import models
from users.models import Profile
from destinations.models import Destination

class Trip(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    destinations = models.ManyToManyField(Destination, related_name="trips")
    image = models.ImageField(upload_to='trip_images/', null=True, blank=True)  # Field for trip images
    activities = models.TextField(null=True, blank=True)  # Field for activities, can store as text

    def __str__(self):
        return self.title
