try:
    from travelers_project.settings.developer import *
except ModuleNotFoundError:
    from travelers_project.settings.production import *
