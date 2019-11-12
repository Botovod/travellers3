from django.urls import path

from laboratory.views import TopCitiesList

urlpatterns = [
    path('topcities', TopCitiesList.as_view(), name='top-cities-url'),
]
