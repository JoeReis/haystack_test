from django.conf.urls import patterns, include, url
from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView

from .forms import GeoForm
from .search_indexes import GeoIndex

from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery

urlpatterns = patterns('haystack.views',



    url(r'^$', SearchView(
        template="geo/geo.html",
        form_class=GeoForm,
    ), name='haystack_search')
)
