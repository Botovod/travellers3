import graphene
from graphene_django.types import DjangoObjectType

from geography.models import City


class CityType(DjangoObjectType):
    class Meta:
        model = City


class Query(graphene.ObjectType):
    all_cities = graphene.List(CityType)
    city = graphene.Field(CityType, id=graphene.Int(), title=graphene.String())

    def resolve_all_cities(self, info, **kwargs):
        return City.objects.all()

    def resolve_city(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')
        if id:
            return City.objects.get(pk=id)

        if title:
            return City.objects.get(title=title)
        return None
