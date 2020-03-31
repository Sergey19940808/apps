from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import AppViewSet

router = DefaultRouter()
router.register(r'', AppViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]