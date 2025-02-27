from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    attractions = models.TextField()
    image = models.ImageField(upload_to='destination_images/', null=True, blank=True)  # Field for destination images
    activities = models.TextField(null=True, blank=True)  # Field for destination activities

    def __str__(self):
        return self.name
