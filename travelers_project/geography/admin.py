from django.contrib import admin

from geography.models import Region, City, TypeOfSights, Sight, SectionOfSights, SightPhoto


class SightPhotoInline(admin.TabularInline):
    model = SightPhoto


class SightAdmin(admin.ModelAdmin):
    inlines = [SightPhotoInline]
    list_display = ('title', 'text')
    list_display_links = ('title', 'text')


admin.site.register(Region)
admin.site.register(City)
admin.site.register(TypeOfSights)
admin.site.register(Sight, SightAdmin)
admin.site.register(SectionOfSights)
