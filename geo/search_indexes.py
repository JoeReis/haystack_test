from haystack import indexes
from .models import Geo


class GeoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #location = indexes.LocationField(model_attr='get_location')
    location = indexes.LocationField()
    latitude = indexes.FloatField(model_attr='latitude')
    longitude = indexes.FloatField(model_attr='longitude')
    zip_code = indexes.CharField(model_attr='zip_code')

    def get_model(self):
        return Geo

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def prepare_location(self, obj):
        # If you're just storing the floats...
        return "%s,%s" % (obj.latitude, obj.longitude)
