from django.urls import path
from .views import FutureTripCityList, CompleteTripCityList, FutureTripSightList, CompleteTripSightList

urlpatterns = [
    path('future-trips-cities/', FutureTripCityList.as_view(), name='future_trip_city_url'),
    path('complete-trips-cities/', CompleteTripCityList.as_view(), name='complete_trip_city_list_url'),
    path('future-trips-sights/', FutureTripSightList.as_view(), name='future_trip_sight_url'),
    path('complete-trips-sights/', CompleteTripSightList.as_view(), name='complete_trip_sight_url'),

]
