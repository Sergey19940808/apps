from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from apps.models import App
from apps.serializers import AppSerializer


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer

    def update(self, request, *a, **kw):
        if request.data.get('key_api'):
            raise APIException({'status': 'Поле key_api нельзя менять через этот метод'})
        return super().update(request, *a, **kw)

    @action(detail=True, methods=['PUT'], url_path='update_key_api')
    def update_key_api(self, request, *a, **kw):
        app = self.get_object()
        key_api = request.data.get('key_api')
        if key_api:
            app.key_api = key_api
            app.save()
            return Response({'status': 'key_api updated'})
        else:
            raise APIException({'status': 'key_api is empty'})

    @action(detail=False, methods=['GET'], url_path='test')
    def filter_by_key_api(self, request, *a, **kw):
        key_api = request.query_params.get('key_api')
        if key_api:
            app = App.objects.filter(key_api=key_api).first()
            return Response(AppSerializer(app).data)
        else:
            raise APIException({'status': 'Not found app with this key_api'})
