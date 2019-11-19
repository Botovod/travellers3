from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('geography.urls')),
    path('traces/', include('traces.urls')),
    path('feedback/', include('feedback.urls')),
    path('laboratory/', include('laboratory.urls')),
    path('graphql/', GraphQLView.as_view(graphiql=True))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
