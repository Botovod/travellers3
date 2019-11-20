from PIL import Image
from django.conf import settings
import os


class RGBConvert:

    def __init__(self, modul=Image):
        self.modul = modul

    @property
    def get_modul(self):
        return self.modul


class ImageConvert:

    def __init__(self, path, modul=RGBConvert()):
        self.modul = modul.get_modul
        self.path = path

    @property
    def convert_rgb(self):
        return self.modul.open(self.path).convert('RGB')


class GetNormalImage:

    def __init__(self, obj, convector=ImageConvert):
        self.obj = obj
        self.convector = convector

    @property
    def _get_path(self):    # Полный путь до изображения
        return os.path.join(settings.MEDIA_ROOT, str(self.obj.file))

    @property
    def _rgb(self):     # Конвектирует файл в "RGB"
        return self.convector(self._get_path).convert_rgb

    @property
    def _get_format(self):      # Возвращает относительный путь до файла без формата
        return str(self.obj.file).split('.')[0]

    @property
    def _save_new_image(self):      # Сохроняет новое изображение рядом со старым с новым форматом
        path_to_new_file = os.path.join(settings.MEDIA_ROOT, f"{self._get_format}.jpg")
        self._rgb.save(path_to_new_file)

    @property
    def _remove(self):          # Удаляет старое изображение
        os.remove(self._get_path)

    @property
    def _save_in_db(self):     # Сохроняет в БД новое изображение
        self.obj.file = f'{self._get_format}.jpg'
        self.obj.save()

    def get_image(self):
        self._save_new_image
        self._remove
        self._save_in_db
