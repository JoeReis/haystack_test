from django import forms

from .models import Geo

from haystack.forms import SearchForm
from haystack.query import SearchQuerySet
from haystack.utils.geo import Point, D


class GeoForm(SearchForm):
    DISTANCE_5 = '5'
    DISTANCE_10 = '10'
    DISTANCE_25 = '25'
    DISTANCE_50 = '50'
    DISTANCE_100 = '100'
    DISTANCE_CHOICES = (
        (DISTANCE_5, DISTANCE_5),
        (DISTANCE_10, DISTANCE_10),
        (DISTANCE_25, DISTANCE_25),
        (DISTANCE_50, DISTANCE_50),
        (DISTANCE_100, DISTANCE_100),
    )

    distance = forms.ChoiceField(choices=DISTANCE_CHOICES)


    def search(self):
        if not self.is_valid():
            return self.no_query_found()

        if not self.cleaned_data['q']:
            return self.no_query_found()

        sqs = self.searchqueryset.all()


        distance = D(mi=self.cleaned_data['distance'])

        obj= Geo.objects.get(zip_code=self.cleaned_data['q'])

        latitude = obj.latitude
        longitude = obj.longitude

        center_point = Point(longitude, latitude)

        sqs = sqs.dwithin('location', center_point, distance)

        if self.load_all:
            sqs.load_all()
            return sqs



