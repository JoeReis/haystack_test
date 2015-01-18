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
        (DISTANCE_5, '5'),
        (DISTANCE_10, '10'),
        (DISTANCE_25, '25'),
        (DISTANCE_50, '50'),
        (DISTANCE_100, '100'),
    )

    #zip_code = forms.CharField(required=True) #this will also be the search term
    distance = forms.ChoiceField(choices=DISTANCE_CHOICES)


    def search(self):
        if not self.is_valid():
            return self.no_query_found()

        sqs = self.searchqueryset

        distance = D(mi=self.cleaned_data['distance'])

        q = self.cleaned_data['q']
        obj= Geo.objects.get(zip_code=self.cleaned_data['q'])
        latitude = obj.latitude
        longitude = obj.longitude


        sqs = SearchQuerySet().dwithin('location', Point(longitude, latitude), distance)

        return sqs


