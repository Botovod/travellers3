from django.views.generic import DetailView
from django.views.generic import ListView

from traces.models import RouteByCities
from traces.models import RouteBySights


class RouteByCitiesList(ListView):
    model = RouteByCities
    context_object_name = 'route_cities_list'
    template_name = 'traces/route_cities_list.html'


class RouteByCitiesDetail(DetailView):
    model = RouteByCities
    context_object_name = 'route_city_detail'
    template_name = 'traces/route_cities_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        index_middle_city = len(self.object.cities.all()) // 2
        context['middle_city'] = self.object.cities.all()[index_middle_city]
        return context


class RouteBySightsList(ListView):
    model = RouteBySights
    context_object_name = 'route_sights_list'
    template_name = 'traces/route_sights_list.html'
    paginate_by = 2


class RouteBySightsDetail(DetailView):
    model = RouteBySights
    context_object_name = 'route_sight_detail'
    template_name = 'traces/route_sights_detail.html'
