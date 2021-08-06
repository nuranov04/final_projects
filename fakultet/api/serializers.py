from rest_framework import serializers
from fakultet.models import *


class FacultyListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'
