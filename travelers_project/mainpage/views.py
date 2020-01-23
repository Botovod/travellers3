from django.views.generic import TemplateView
from .models import MainPage


class IndexView(TemplateView):
    template_name = "mainpage/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page'] = MainPage.objects.first()
        return context
