from django.urls import path
from .views import home, brand_by_car, car_detail, save_comment
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('brand/<int:brand_id>/', brand_by_car, name='by_brand'),
    path('car/<int:pk>/', car_detail, name='by_car'),
    path('comment/save/<int:car_id>/', save_comment, name='save_comment'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)