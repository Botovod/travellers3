from django.urls import path
from . import views

urlpatterns = [
    path('', views.region_list, name='region_list_url'),
    path('region/<int:pk>/', views.region_detail, name='region_detail_url'),
    path('city/<int:pk>/', views.city_detail, name='city_detail_url'),
    path('type-sights/', views.type_sights, name='type_sights_url'),
    path('type-sights/<int:pk>/', views.type_sight_detail, name='type_sight_detail_url'),
]
