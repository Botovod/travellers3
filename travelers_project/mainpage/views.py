from django.views.generic import TemplateView, ListView
from .models import MainPage
from trips.views import CompleteTripCityList, FutureTripCityList
from datetime import date
from trips.models import CityTrip


class IndexView(TemplateView):
    template_name = "mainpage/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page'] = MainPage.objects.first()
        context['recent_trips'] = CityTrip.objects.filter(end_date__date__lt=date.today()).order_by('end_date')[:4]
        context['future_trips'] = CityTrip.objects.filter(start_date__date__gt=date.today()).order_by('start_date')[:4]
        return context
