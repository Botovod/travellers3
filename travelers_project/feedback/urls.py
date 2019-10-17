from django.urls import path
from feedback.views import FeedbackView, DoneView

urlpatterns = [
    path('', FeedbackView.as_view(), name='feedback_url'),
    path('done/', DoneView.as_view(), name='done_url'),
]
