#from django.contrib.gis.geos import Pointet20144

from django.db import models
from django.contrib.gis.geos import Point


class Geo(models.Model):
    DISTANCE_5 = '5'
    DISTANCE_10 = '10'
    DISTANCE_25 = '25'
    DISTANCE_50 = '50'
    DISTANCE_100 = '100'
    DISTANCE_CHOICES = (
        (DISTANCE_5, '5'),
        (DISTANCE_10, '10'),
        (DISTANCE_25, '25'),
        (DISTANCE_50, '50'),
        (DISTANCE_100, '100'),
    )

    distance = models.CharField(max_length=4, choices=DISTANCE_CHOICES, default=DISTANCE_5)
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
