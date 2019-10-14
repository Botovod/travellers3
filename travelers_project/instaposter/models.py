from django.db import models
from instaposter.utils import load_image

class Post(models.Model):
    comment = models.TextField()
    image = models.ImageField(upload_to=load_image)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return f'{self.comment[:20]}....'
