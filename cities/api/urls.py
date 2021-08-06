from cities.api.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'cities', CityViewSet, basename='cities')
router.register(r'city_images', CityImageViewSet, basename='city_images')
router.register(r'universities', UniversityViewSet, basename='universities')


urlpatterns = router.urls
