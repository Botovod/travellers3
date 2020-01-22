from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "mainpage/index.html"
