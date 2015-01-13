from django import forms
from haystack.forms import SearchForm


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

    zip_code = forms.CharField(required=True)
    distance = forms.ChoiceField(choices=DISTANCE_CHOICES)
