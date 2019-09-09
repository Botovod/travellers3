from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView

from geography.models import Sight
from travelers.models import Traveler

class BaseTemplate(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwrags):
        context = super().get_context_data(**kwrags)
        context['sights'] = Sight.objects.all()
        return context


class TravelerList(ListView):
    model = Traveler
    context_object_name = 'traveler_list'
    template_name = 'travelers/index.html'


class TravelerDetail(DetailView):
    model = Traveler
    template_name = 'travelers/traveler_detail.html'
    context_object_name = 'traveler_detail'
