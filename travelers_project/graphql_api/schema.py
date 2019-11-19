import graphene
from graphene_django.types import DjangoObjectType

from geography.models import City, Region


class CityType(DjangoObjectType):
    class Meta:
        model = City


class RegionType(DjangoObjectType):
    class Meta:
        model = Region


class Query(graphene.ObjectType):
    all_cities = graphene.List(CityType)
    region = graphene.Field(RegionType, title=graphene.String())

    def resolve_all_cities(self, info, **kwargs):
        return City.objects.all()

    def resolve_region(self, info, **kwargs):
        title = kwargs.get('title')

        if title:
            return Region.objects.get(title=title)
        return None
