from django.urls import path

from .views import RouteByCitiesDetail
from .views import RouteByCitiesList
from .views import RouteBySightsDetail
from .views import RouteBySightsList

urlpatterns = [
    # ex: traces/route_cities
    path('route-cities/', RouteByCitiesList.as_view()),
    # ex: traces/route_cities/1/
    path('route-cities/<int:pk>/', RouteByCitiesDetail.as_view()),
    # ex: traces/route_sigths
    path('route-sights/', RouteBySightsList.as_view()),
    # ex: traces/route_sights/1/
    path('route-sights/<int:pk>/', RouteBySightsDetail.as_view()),
]
