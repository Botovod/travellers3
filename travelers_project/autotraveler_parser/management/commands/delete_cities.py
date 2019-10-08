import os
import shutil
from django.conf import settings
from geography.models import City
from django.core.management.base import BaseCommand

# Clean test's objects
class Command(BaseCommand):

    def handle(self, *args, **kwrags):
        City.objects.all().delete()

        folder_with_images = os.path.join(settings.MEDIA_ROOT, 'images/cities')

        dirs_with_images = os.listdir(folder_with_images)

        for dir in dirs_with_images:
            shutil.rmtree(os.path.join(folder_with_images, dir))

        print("All is deleted!!!")
