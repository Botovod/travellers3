from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView

from sorl.thumbnail import get_thumbnail

from geography.models import Sight

from travelers_project.settings import DEFAULT_PHOTO_PATH


class BaseTemplate(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sights'] = Sight.objects.all()[:4]

        try:
            file = open(DEFAULT_PHOTO_PATH)
            default_image = get_thumbnail(file, 'x150', crop='center')
            context['default_image'] = default_image
        except FileExistsError:
            pass

        return context
