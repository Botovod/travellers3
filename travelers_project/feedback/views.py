from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from feedback.models import Feedback
from feedback.forms import FeedbackForm


class FeedbackView(FormView):
    template_name = 'feedback/contact.html'
    form_class = FeedbackForm
    success_url = 'done/'

    def form_valid(self, form):
        form.mail()
        form.save()
        return super().form_valid(form)

class DoneView(TemplateView):
    template_name = 'feedback/done.html'
