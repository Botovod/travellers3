from django.urls import path

from laboratory.views import TopCitiesList
from laboratory.views import TopTracesListView

urlpatterns = [
    path('topcities', TopCitiesList.as_view(), name='top-cities-url'),
    path('toptraces/', TopTracesListView.as_view(), name='top_traces_url'),
]
