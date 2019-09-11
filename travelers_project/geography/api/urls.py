from django.urls import path

from geography.api.views import RegionList
from geography.api.views import RegionDetail

urlpatterns = [
    path('regions/', RegionList.as_view()),
    path('regions/<int:pk>/', RegionDetail.as_view()),

]
