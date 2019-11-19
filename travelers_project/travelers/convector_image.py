from PIL import Image
from django.conf import settings
import os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(path)
#
# img = Image.open(f"{path}/1.png")
# rgb_im = img.convert('RGB')
# rgb_im.save(f'{path}/1-rgb.jpg')
#
# img_2 = Image.open(f"{path}/1-rgb.jpg")
# img_2.show()


def convector_to_sight(obj):
    path = os.path.join(settings.MEDIA_ROOT, str(obj.file))

    old_image = Image.open(path)
    new_image = old_image.convert('RGB')

    pattern = str(obj.file).split('.')
    new_image.save(os.path.join(settings.MEDIA_ROOT, f'{pattern[0]}.jpg'))
    os.remove(path)
    obj.file = f'{pattern[0]}.jpg'
    obj.save()
