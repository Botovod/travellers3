from django.core.mail import send_mail
from django.conf import settings

class Message:

    def __init__(self, name, message, to=[]):

        self.name = name
        self.message = message
        self.to = to

    def send_email(self):
        subject = f"Feedback from {self.name}."
        self.to.append(settings.EMAIL_HOST_USER)

        mail = send_mail(
                    subject,
                    self.message,
                    settings.EMAIL_HOST_USER,
                    self.to
                )
        return mail
