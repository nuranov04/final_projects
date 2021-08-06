from fakultet.api.serializers import *
from fakultet.models import *
from rest_framework import viewsets


class FacultyListViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultyListSerializers

