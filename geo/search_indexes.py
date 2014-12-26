from haystack import indexes
from .models import Geo


class GeoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    zip = indexes.CharField(model_attr='zip')
    latitude = indexes.CharField(model_attr='latitude')
    longitude = indexes.CharField(model_attr='longitude')

    def get_models(self):
        return Geo
