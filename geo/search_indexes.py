from haystack import indexes
from .models import Geo


class GeoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    zip = indexes.CharField(model_attr='zip')
    location = indexes.LocationField(model_attr='get_location')

    def get_model(self):
        return Geo
