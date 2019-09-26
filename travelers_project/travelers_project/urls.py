from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('travelers.urls')),
    path('geography/', include('geography.urls')),
<<<<<<< HEAD
    path('travelers/', include('travelers.urls')),
=======
    path('traces/', include('traces.urls')),
    path('api/v1/geography/', include('geography.api.urls')),

>>>>>>> 2218f58066aa793c09d6c3e0a7fe0ef3a26f0fa0
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
