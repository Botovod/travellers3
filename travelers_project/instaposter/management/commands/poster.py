from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from instaposter.models import Post
from django.conf import settings
from instapy_cli import client
import logging
import os

logger = logging.getLogger(__name__)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        username = settings.INST_USERNAME
        password = settings.INST_PASSWORD
        # cookie_file = os.path.join(settings.BASE_DIR, 'travelers_project/user_ig.json')

        try:
            post = Post.objects.first()
        except ObjectDoesNotExist as e:
            post = ''
            logger.error(e)

        if post:
            image = os.path.join(settings.MEDIA_ROOT, str(post.image))
            text = post.comment

            with client(username, password) as cli:
                cli.upload(image, text)
                print(f"Post {text[:10]}... Done!!!")
