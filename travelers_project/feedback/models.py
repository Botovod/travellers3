from django.db import models

class Feedback(models.Model):
    fullname = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.fullname
