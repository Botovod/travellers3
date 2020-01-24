from django.views.generic import DetailView, ListView
from .models import SightTrip, CityTrip
from datetime import date


class BaseTrip(ListView):
    template_name = 'trips/trips.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.page_title
        return context


class CompleteTripMixin(object):
    ordering = ['-end_date']

    def get_queryset(self):
        return super().get_queryset().filter(end_date__date__lt=date.today())


class FutureTripMixin(object):
    ordering = ['start_date']

    def get_queryset(self):
        return super().get_queryset().filter(start_date__date__gt=date.today())


class FutureTripCityList(FutureTripMixin, BaseTrip):
    model = CityTrip
    page_title = 'Планируемые путешествия по городам'


class CompleteTripCityList(CompleteTripMixin, BaseTrip):
    model = CityTrip
    page_title = 'Завершенные путешествия по городам'


class FutureTripSightList(FutureTripMixin, BaseTrip):
    model = SightTrip
    page_title = 'Планируемые путешествия по достопримечательностям'


class CompleteTripSightList(CompleteTripMixin, BaseTrip):
    model = SightTrip
    page_title = 'Завершенные путешествия по достопримечательностям'
