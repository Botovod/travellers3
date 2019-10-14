import os
from datetime import datetime
from time import time

def load_image(instance, filename):
    format = filename.split('.')[-1]
    filename = "file-{}.{}".format(time() * 1000, format)
    path = "/".join(["poster", datetime.strftime(datetime.now(), '%Y/%m/%d')])
    return os.path.join(path, filename)
