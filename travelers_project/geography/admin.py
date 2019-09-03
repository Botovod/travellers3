from django.contrib import admin
from .models import (
    Region, City, TypeOfSights, Sight, SectionOfSights, SightPhoto
)


class SightPhotoInline(admin.TabularInline):
    model = SightPhoto


@admin.register(Sight)
class SightAdmin(admin.ModelAdmin):
    inlines = [SightPhotoInline]

admin.site.register(Region)
admin.site.register(City)
admin.site.register(TypeOfSights)
admin.site.register(SectionOfSights)
