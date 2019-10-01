from django.urls import path
from geography import views

urlpatterns = [
    path('', views.RegionList.as_view(), name='region_list_url'),
    path('region/<int:pk>/', views.RegionDetail.as_view(), name='region_detail_url'),
    path('cities/', views.CityList.as_view(), name='city_list_url'),
    path('city/<int:pk>/', views.CityDetail.as_view(), name='city_detail_url'),
    path('sights/', views.SightList.as_view(), name='sight_list_url'),
    path('sight/<int:pk>/', views.SightDetail.as_view(), name='sight_detail_url'),

    # api v1
    path('api/v1/regions/', views.RegionListAPI.as_view()),
    path('api/v1/region/<int:pk>/', views.RegionDetailAPI.as_view()),
    path('api/v1/cities/', views.CityListAPI.as_view()),
    path('api/v1/city/<int:pk>/', views.CityDetailAPI.as_view()),
    path('api/v1/sights/', views.SightListAPI.as_view()),
    path('api/v1/sight/<int:pk>/', views.SightDetailAPI.as_view()),
    path('api/v1/sightphotos/', views.SightPhotoListAPI.as_view()),
    path('api/v1/sightphoto/<int:pk>/', views.SightPhotoDetailAPI.as_view()),
    path('api/v1/sectionofsights/', views.SectionOfSightsListAPI.as_view()),
    path('api/v1/sectionofsights/<int:pk>/', views.SectionOfSightsDetailAPI.as_view()),
    path('api/v1/typeofsights/', views.TypeOfSightsListAPI.as_view()),
    path('api/v1/typeofsights/<int:pk>/', views.TypeOfSightsDetailAPI.as_view()),
]
