from rest_framework import generics
from cities.api.serilazers import *
from cities.models import *
from rest_framework import viewsets


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CityListSerializers


class CityImageViewSet(viewsets.ModelViewSet):
    queryset = CityImage.objects.all()
    serializer_class = CitiImageSerializers


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversityListSerializers
