from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView

from sorl.thumbnail import get_thumbnail

from geography.models import Sight


class BaseTemplate(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sights'] = Sight.objects.all()[:4]

        return context
