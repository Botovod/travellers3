from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Traveler


class TravelerList(ListView):
    model = Traveler
    context_object_name = 'traveler_list'
    template_name = 'travelers/index.html'


class TravelerDetail(DetailView):
    model = Traveler
    template_name = 'travelers/traveler_detail.html'
    context_object_name = 'traveler_detail'
