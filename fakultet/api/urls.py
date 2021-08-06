from fakultet.api.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'faculties', FacultyListViewSet, basename='faculties')

urlpatterns = router.urls
