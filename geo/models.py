from django.db import models


class Geo(models.Model):
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=10)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    timezone = models.CharField(max_length=5)
    dst = models.CharField(max_length=5)
