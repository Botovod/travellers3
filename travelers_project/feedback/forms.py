from django import forms
from feedback.utils import Message
from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput)

    class Meta:
        model = Feedback
        fields = ['fullname', 'text', 'email']

    def save(self):
        feedback = Feedback.objects.create(
            fullname=self.cleaned_data['fullname'],
            email=self.cleaned_data['email'],
            text=self.cleaned_data['text'],
        )
        return feedback

    def mail(self):
        mail = Message(
            self.cleaned_data['fullname'],
            self.cleaned_data['text'],
            [self.cleaned_data['email']]
            )
        mail.send_email()
