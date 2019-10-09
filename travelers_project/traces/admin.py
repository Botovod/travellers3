from django.contrib import admin

from traces.models import RouteByCities, CitiesRelationship
from traces.models import RouteBySights, SightsRelationship


class SightsRelationshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'sight', 'route', 'position')
    list_display_links = ('sight', 'route', 'position')
    search_fields = ['id', 'sight']


admin.site.register(RouteByCities)
admin.site.register(RouteBySights)
admin.site.register(CitiesRelationship)
admin.site.register(SightsRelationship, SightsRelationshipAdmin)
