from django.views.generic import DetailView, ListView
from .models import SightTrip, CityTrip
from datetime import date


class CompleteTripMixin(object):
    template_name = 'trips/trips.html'
    paginate_by = 5
    ordering = ['-end_date']

    def get_queryset(self):
        return super().get_queryset().filter(end_date__date__lt=date.today())


class FutureTripMixin(object):
    template_name = 'trips/trips.html'
    paginate_by = 5
    ordering = ['start_date']

    def get_queryset(self):
        return super().get_queryset().filter(start_date__date__gt=date.today())


class FutureTripCityList(FutureTripMixin, ListView):
    model = CityTrip

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Планируемые путешествия по городам'
        return context


class CompleteTripCityList(CompleteTripMixin, ListView):
    model = CityTrip

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Завершенные путешествия по городам'
        return context


class FutureTripSightList(FutureTripMixin, ListView):
    model = SightTrip

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Планируемые путешествия по достопримечательностям'
        return context


class CompleteTripSightList(CompleteTripMixin, ListView):
    model = SightTrip

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Завершенные путешествия по достопримечательностям'
        return context
