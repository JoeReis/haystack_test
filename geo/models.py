from django.db import models


class Geo(models.Model):
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timezone = models.CharField(max_length=5, blank=True, null=True)
    dst = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.zip
