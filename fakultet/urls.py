from django.urls import path, include
from fakultet.views import all_faculty, faculty_detail, create_faculty
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('all_faculties/', all_faculty, name='all_faculties'),
    path('faculty_detail/<int:id>', faculty_detail, name='faculty_detail'),
    path('create_faculty/', create_faculty, name='create_faculty'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
