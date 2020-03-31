from rest_framework import viewsets

from apps.models import App
from apps.serializers import AppSerializer


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
