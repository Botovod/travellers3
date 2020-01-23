from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from rest_framework_swagger.views import get_swagger_view

from graphene_django.views import GraphQLView

API_TITLE = 'Travelers API'
API_DESCRIPTION = 'A Web API for creating and editing objects'
schema_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainpage.urls')),
    path('', include('geography.urls')),
    path('', include('trips.urls')),
    path('traces/', include('traces.urls')),
    path('feedback/', include('feedback.urls')),
    path('laboratory/', include('laboratory.urls')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger-docs/', schema_view)

]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
