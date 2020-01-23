from django.views.generic import DetailView, ListView
from .models import SightTrip, CityTrip
from datetime import date


class FutureTripCityList(ListView):
    queryset = CityTrip.objects.filter(start_date__date__gt=date.today())
    context_object_name = 'future_trip_city_list'
    template_name = 'trips/future_trip_city_list.html'
    ordering = ['start_date']
    paginate_by = 5


class CompleteTripCityList(ListView):
    queryset = CityTrip.objects.filter(end_date__date__lt=date.today())
    context_object_name = 'complete_trip_city_list'
    template_name = 'trips/complete_trip_city_list.html'
    paginate_by = 5
    ordering = ['-end_date']


class FutureTripSightList(ListView):
    queryset = SightTrip.objects.filter(start_date__date__gt=date.today())
    context_object_name = 'future_trip_sight_list'
    template_name = 'trips/future_trip_sight_list.html'
    paginate_by = 5
    ordering = ['start_date']


class CompleteTripSightList(ListView):
    queryset = SightTrip.objects.filter(end_date__date__lt=date.today())
    context_object_name = 'complete_trip_sight_list'
    template_name = 'trips/complete_trip_sight_list.html'
    paginate_by = 5
    ordering = ['-end_date']
