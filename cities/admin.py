from django.contrib import admin
from .models import City, University,CityImage,UniversityImage

admin.site.register(University)
admin.site.register(UniversityImage)
admin.site.register(City)
admin.site.register(CityImage)