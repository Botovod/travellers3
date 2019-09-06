from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegionList.as_view(), name='region_list_url'),
    path('region/<int:pk>/', views.RegionDetail.as_view(), name='region_detail_url'),
    path('cities/', views.CityList.as_view(), name='city_list'),
    path('city/<int:pk>/', views.CityDetail.as_view(), name='city_detail_url'),
    path('sights/', views.SightList.as_view(), name='sight_list'),
    path('sight/<int:pk>/', views.SightDetail.as_view(), name='sight_detail')
]
