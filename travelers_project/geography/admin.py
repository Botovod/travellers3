from django.contrib import admin

from geography.models import Region, City, TypeOfSights, Sight, SectionOfSights, SightPhoto


class SightPhotoInline(admin.TabularInline):
    model = SightPhoto


class SightAdmin(admin.ModelAdmin):
    inlines = [SightPhotoInline]
    list_display = ('title', 'text')
    list_display_links = ('title', 'text')


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'region', 'description')
    list_display_links = ('title', 'region', 'description')
    search_fields = ['id', 'title']


admin.site.register(Region)
admin.site.register(City, CityAdmin)
admin.site.register(TypeOfSights)
admin.site.register(Sight, SightAdmin)
admin.site.register(SectionOfSights)
