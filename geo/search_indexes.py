from haystack import indexes
from .models import Geo


class GeoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    location = indexes.LocationField(model_attr='get_location')
    latitude = indexes.FloatField(model_attr='latitude')
    longitude = indexes.FloatField(model_attr='longitude')
    zip_code = indexes.CharField(model_attr='zip_code')

    def get_model(self):
        return Geo

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
