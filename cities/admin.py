from django.contrib import admin
from cities import models


class CityImageAdmin(admin.TabularInline):
    model = models.CityImage
    extra = 3


class CityAdmin(admin.ModelAdmin):
    list_display = ['city']
    search_fields = ['city']
    inlines = [CityImageAdmin]


class UniversityImageAdmin(admin.TabularInline):
    model = models.UniversityImage
    extra = 3


class UniversityAdmin(admin.ModelAdmin):
    list_display = ['university']
    search_fields = ['university']
    inlines = [UniversityImageAdmin]


admin.site.register(models.University, UniversityAdmin)
admin.site.register(models.City, CityAdmin)
