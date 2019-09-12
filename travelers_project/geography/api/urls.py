from django.urls import path

from geography.api.views import RegionList
from geography.api.views import RegionDetail
from geography.api.views import CityList
from geography.api.views import CityDetail

urlpatterns = [
    path('regions/', RegionList.as_view()),
    path('region/<int:pk>/', RegionDetail.as_view()),
    path('cities/', CityList.as_view()),
    path('city/<int:pk>/', CityDetail.as_view()),

]
