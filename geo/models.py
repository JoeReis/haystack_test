#from django.contrib.gis.geos import Pointet20144

from django.db import models
from django.contrib.gis.geos import Point


class Geo(models.Model):
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timezone = models.CharField(max_length=5, blank=True, null=True)
    dst = models.CharField(max_length=5, blank=True, null=True)

    def get_location(self):
        return Point(self.longitude, self.latitude)

    def __str__(self):
        return self.zip_code
