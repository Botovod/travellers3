from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('geography/', include('geography.urls')),
    path('travelers/', include('travelers.urls')),

]
