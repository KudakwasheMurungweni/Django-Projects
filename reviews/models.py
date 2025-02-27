from django.db import models
from users.models import Profile
from trips.models import Trip

class Review(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'Review for {self.trip.title} by {self.user.user.username}'
