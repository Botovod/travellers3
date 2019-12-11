from django.urls import path, include

from traces.views import RouteByCitiesList, RouteByCitiesDetail
from traces.views import RouteBySightsList, RouteBySightsDetail


urlpatterns = [
    path('route-cities/', RouteByCitiesList.as_view(), name='routes-cities-list-url'),
    path('route-cities/<int:pk>/', RouteByCitiesDetail.as_view(), name='routes-cities-detail-url'),
    path('route-sights/', RouteBySightsList.as_view(), name='routes-sights-list-url'),
    path('route-sights/<int:pk>/', RouteBySightsDetail.as_view(), name='routes-sights-detail-url'),
]
