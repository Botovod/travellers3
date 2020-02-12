from django.urls import path
from .views import FutureTripCityList, CompleteTripCityList, FutureTripSightList, CompleteTripSightList
from .views import FutureCityTripDetail, CompleteTripCityDetail, FutureTripSightDetail, CompleteTripSightDetail

urlpatterns = [
    path('future-trips-cities/', FutureTripCityList.as_view(), name='future_trip_city_url'),
    path('future-trips-cities/<int:pk>/', FutureCityTripDetail.as_view(), name='future_trip_city_detail_url'),
    path('complete-trips-cities/', CompleteTripCityList.as_view(), name='complete_trip_city_list_url'),
    path('complete-trips-cities/<int:pk>/', CompleteTripCityDetail.as_view(), name='complete_trip_city_detail_url'),
    path('future-trips-sights/', FutureTripSightList.as_view(), name='future_trip_sight_url'),
    path('future-trips-sights/<int:pk>/', FutureTripSightDetail.as_view(), name='future_trip_sight_detail_url'),
    path('complete-trips-sights/', CompleteTripSightList.as_view(), name='complete_trip_sight_url'),
    path('complete-trips-sights/<int:pk>/', CompleteTripSightDetail.as_view(), name='complete_trip_sight_detail_url'),

]
