from django.urls import path

from .views import BaseTemplate
from .views import TravelerDetail
from .views import TravelerList

urlpatterns = [
    # ex: /
    path('', BaseTemplate.as_view(), name='base_url'),
    # ex: /travelers/
    path('travelers/', TravelerList.as_view()),
    # ex: /travelers/5/
    path('travelers/<int:pk>/', TravelerDetail.as_view()),

]
