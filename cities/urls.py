from django.urls import path, include
from .views import (
    all_universities,
    index,
    university_detail,
    city_detail,
    create_city
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('all_universities', all_universities, name='all_universities'),
    path('university_detail/<int:id>/', university_detail, name='university'),
    path('city_detail/<int:id>/', city_detail, name='city'),
    path('create_city/', create_city, name='create_city'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
