from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from posts.views import *

router = routers.SimpleRouter()
router.register(r'actor', ActorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
