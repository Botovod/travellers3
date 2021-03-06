import graphene
from graphene_django.types import DjangoObjectType
from django.db.models import Max

from geography.models import City, Region, Sight, SightPhoto
from traces.models import RouteByCities, CitiesRelationship


class CityType(DjangoObjectType):
    class Meta:
        model = City


class RegionType(DjangoObjectType):
    class Meta:
        model = Region


class SightType(DjangoObjectType):
    class Meta:
        model = Sight


class SightPhotoType(DjangoObjectType):
    class Meta:
        model = SightPhoto


class CityTraceType(DjangoObjectType):
    class Meta:
        model = RouteByCities


class CitiesRelationshipType(DjangoObjectType):
    class Meta:
        model = CitiesRelationship


class Query(graphene.ObjectType):
    all_cities = graphene.List(CityType)
    all_regions = graphene.List(RegionType)
    region = graphene.Field(RegionType, id=graphene.Int(), title=graphene.String())
    best_cities = graphene.List(CityType, id=graphene.Int())
    best_sight_in_region = graphene.List(SightType, id=graphene.Int())
    best_sightphoto_in_region = graphene.List(SightPhotoType, id=graphene.Int())
    sights_in_city = graphene.List(SightType, id=graphene.Int())
    photos_in_sight = graphene.List(SightPhotoType, id=graphene.Int())

    city_traces = graphene.List(CityTraceType)
    cities_in_trace = graphene.List(CitiesRelationshipType, id=graphene.Int(), title=graphene.String())
    best_sights_in_trace = graphene.List(SightType, id=graphene.Int())

    def resolve_all_cities(self, info, **kwargs):
        return City.objects.all()

    def resolve_region(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id:
            return Region.objects.get(id=id)

        if title:
            return Region.objects.get(title=title)
        return None

    def resolve_best_cities(self, info, **kwargs):
        region_id = kwargs.get('id')
        cities = City.objects.filter(region=region_id)
        city_max = cities.aggregate(Max('rating'))
        filtered_cities = cities.filter(rating=city_max['rating__max'])

        if region_id:
            return filtered_cities
        return None

    def resolve_sights_in_city(self, info, **kwargs):
        city_id = kwargs.get('id')
        sights = Sight.objects.filter(city=City.objects.get(id=city_id))

        if city_id:
            return sights
        return None

    def resolve_all_regions(self, info, **kwargs):
        return Region.objects.all()

    def resolve_best_sight_in_region(self, info, **kwargs):
        region_id = kwargs.get('id')
        sights = Sight.objects.filter(city__in=City.objects.filter(region=region_id))
        sight_max = sights.aggregate(Max('rating'))
        filtered_sights = sights.filter(rating=sight_max['rating__max'])

        if region_id:
            return filtered_sights
        return None

    def resolve_photos_in_sight(self, info, **kwargs):
        sight_id = kwargs.get('id')
        photos = SightPhoto.objects.filter(sight=Sight.objects.get(id=sight_id))

        if sight_id:
            return photos
        return None

    def resolve_best_sightphoto_in_region(self, info, **kwargs):
        region_id = kwargs.get('id')
        sights = Sight.objects.filter(city__in=City.objects.filter(region=region_id))
        photos = SightPhoto.objects.filter(sight__in=sights)
        photo_max = photos.aggregate(Max('rating'))
        filtered_photos = photos.filter(rating=photo_max['rating__max'])

        if region_id:
            return filtered_photos
        return None

    def resolve_city_traces(self, info, **kwargs):
        return RouteByCities.objects.all()

    def resolve_cities_in_trace(self, info, **kwargs):
        trace_id = kwargs.get('id')
        trace_title = kwargs.get('title')
        if trace_id:
            cities = CitiesRelationship.objects.filter(route__in=RouteByCities.objects.filter(id=trace_id))

        if trace_title:
            cities = CitiesRelationship.objects.filter(route__in=RouteByCities.objects.filter(title=trace_title))

        return cities

    def resolve_best_sights_in_trace(self, info, **kwargs):
        trace_id = kwargs.get('id')
        cities_relationship = CitiesRelationship.objects.filter(route__in=RouteByCities.objects.filter(id=trace_id))
        # cities = City.objects.filter(city__in=cities_relationship)
        sights = Sight.objects.filter(sight__in=cities_relationship)
        sight_max = sights.aggregate(Max('rating'))
        filtered_sights = sights.filter(rating=sight_max['rating__max'])
