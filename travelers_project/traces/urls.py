from django.urls import path

from traces.views import RouteByCitiesDetail
from traces.views import RouteByCitiesList
from traces.views import RouteBySightsDetail
from traces.views import RouteBySightsList

urlpatterns = [
    # ex: traces/route_cities
    path('route-cities/', RouteByCitiesList.as_view(), name='routes-cities-list-url'),
    # ex: traces/route_cities/1/
    path('route-cities/<int:pk>/', RouteByCitiesDetail.as_view(), name='routes-cities-detail-url'),
    # ex: traces/route_sigths
    path('route-sights/', RouteBySightsList.as_view()),
    # ex: traces/route_sights/1/
    path('route-sights/<int:pk>/', RouteBySightsDetail.as_view()),
]
