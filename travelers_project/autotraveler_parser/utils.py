import shutil
import os
from slugify import slugify
from django.conf import settings
from time import time


def create_path_for_image(folder, title):

    slug = slugify(title)                                             # перобразуем title в slug

    media_folder = settings.MEDIA_ROOT                                  # Папка media

    slug_folder = f'images/{folder}/{slug}'                              # Папка для с названием (slug)

    path_to_folder_image = os.path.join(media_folder, slug_folder)         # Путь до папки с изображением

    rename = "file-{}.jpg".format(int(time() * 1000))                   # Смена имени файла


    if not os.path.exists(path_to_folder_image):                                                                     # Если нет папки для image создаём её
        os.makedirs(path_to_folder_image)

    path_to_image = os.path.join(path_to_folder_image, rename)                  # Полныйпуть до файла с изображение

    return (path_to_image, os.path.join(slug_folder, rename))
