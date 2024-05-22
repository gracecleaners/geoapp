from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)  # Optional: to categorize locations

    def __str__(self):
        return self.name