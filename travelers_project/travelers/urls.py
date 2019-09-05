from django.urls import path

from .views import TravelerDetail
from .views import TravelerList

urlpatterns = [
    # ex: /travelers/
    path('', TravelerList.as_view()),
    # ex: /travelers/5/
    path('<int:pk>/', TravelerDetail.as_view()),

]
