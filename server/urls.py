from django.contrib import admin
from django.urls import include, re_path, path
from rest_framework.routers import DefaultRouter
from app.views import create_reservation


router = DefaultRouter(trailing_slash=False)


urlpatterns = [
    re_path(r"^api/v1/", include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/forecast', create_reservation),
]
