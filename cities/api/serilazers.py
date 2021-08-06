from rest_framework import serializers
from cities.models import *
from fakultet.api.serializers import *


class CitiImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = CityImage
        fields = "__all__"


class UniversityListSerializers(serializers.ModelSerializer):
    faculty = FacultyListSerializers(many=True, read_only=True)

    class Meta:
        model = University
        fields = "__all__"


class CityListSerializers(serializers.ModelSerializer):
    city_image = CitiImageSerializers(many=True, read_only=True)
    univer = UniversityListSerializers(many=True, read_only=True)

    class Meta:
        model = City
        fields = '__all__'
