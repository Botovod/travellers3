from django.contrib import admin

from .models import Post
from .models import PostPhoto
from .models import Route
from .models import Sourse
from .models import Tag
from .models import Travel
from .models import Traveler

admin.site.register(Travel)
admin.site.register(Traveler)
admin.site.register(Route)
admin.site.register(Sourse)
admin.site.register(Post)
admin.site.register(PostPhoto)
admin.site.register(Tag)
