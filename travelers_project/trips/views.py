from django.views.generic import DetailView, ListView
from .models import SightTrip, CityTrip
from datetime import date


class BaseTrip(ListView):
    template_name = 'trips/trips.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.page_title
        context['url_name'] = self.url
        return context


class BaseTripDetail(DetailView):
    template_name = 'trips/trip_detail.html'


class CityTrips(BaseTrip):
    model = CityTrip


class SightTrips(BaseTrip):
    model = SightTrip


class CompleteTripMixin(object):
    ordering = ['-end_date']

    def get_queryset(self):
        return super().get_queryset().filter(end_date__date__lt=date.today())


class FutureTripMixin(object):
    ordering = ['start_date']

    def get_queryset(self):
        return super().get_queryset().filter(start_date__date__gt=date.today())


class FutureTripCityList(FutureTripMixin, CityTrips):
    page_title = 'Планируемые путешествия по городам'
    url = 'future_trip_city_detail_url'


class CompleteTripCityList(CompleteTripMixin, CityTrips):
    page_title = 'Завершенные путешествия по городам'
    url = 'complete_trip_city_detail_url'


class FutureTripSightList(FutureTripMixin, SightTrips):
    page_title = 'Планируемые путешествия по достопримечательностям'
    url = 'future_trip_sight_detail_url'


class CompleteTripSightList(CompleteTripMixin, SightTrips):
    page_title = 'Завершенные путешествия по достопримечательностям'
    url = 'complete_trip_sight_detail_url'


class FutureCityTripDetail(FutureTripMixin, BaseTripDetail):
    model = CityTrip


class FutureTripSightDetail(FutureTripMixin, BaseTripDetail):
    model = SightTrip


class CompleteTripSightDetail(CompleteTripMixin, BaseTripDetail):
    model = SightTrip


class CompleteTripCityDetail(CompleteTripMixin, BaseTripDetail):
    model = CityTrip
