from django.contrib import admin
from .models import City, University,CityImage

admin.site.register(University)
admin.site.register(City)
admin.site.register(CityImage)