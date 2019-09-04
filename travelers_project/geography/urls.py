from django.urls import path
from .views import regions

urlpatterns = [
    path('', regions, name='regions_url'),
]
