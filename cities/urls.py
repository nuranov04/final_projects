from django.urls import path, include
from .views import (
    all_universities,
    index,
    university_detail,
    city_detail,
    create_city,
    create_university,
    update_city,
    update_university,
    delete_city,
    university_delete,
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('city_detail/<int:id>/', city_detail, name='city'),
    path('update_city/<int:id>/', update_city, name='update_city'),
    path('create_city/', create_city, name='create_city'),
    path('delete_city/<int:id>', delete_city, name='delete_city'),
    path('all_universities', all_universities, name='all_universities'),
    path('university_detail/<int:id>/', university_detail, name='university'),
    path('create_university/', create_university, name='create_university'),
    path('update_university/<int:id>', update_university, name='update_university'),
    path('delete_university/<int:id>', university_delete, name='delete_university'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
