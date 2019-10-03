from django.db import models


class Album(models.Model):
    vk_id = models.PositiveIntegerField(blank=False, null=True, default=0)
    owner_id = models.PositiveIntegerField(blank=False, null=True, default=0)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)

    class Meta:
        unique_together = [['vk_id', 'owner_id']]

    def __str__(self):
        return self.title


def set_image_folder(instance, filename):
    return "user{}/album{}/{}".format(instance.owner_id, instance.album_id, filename)


class Photo(models.Model):
    vk_id = models.PositiveIntegerField(blank=False, null=True, default=0)
    owner_id = models.PositiveIntegerField(blank=False, null=True, default=0)
    album_id = models.PositiveIntegerField(blank=False, null=True, default=0)
    url = models.CharField(max_length=255)
    image = models.ImageField(upload_to=set_image_folder)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return 'Photo {} from album {}'.format(self.vk_id, self.album_id)
