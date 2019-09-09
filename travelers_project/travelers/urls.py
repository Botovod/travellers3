from django.urls import path

from .views import BaseTemplate

urlpatterns = [
    # ex: /
    path('', BaseTemplate.as_view(), name='base_url'),
]
