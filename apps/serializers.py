from rest_framework import serializers

from apps.models import App


class AppSerializer(serializers.ModelSerializer):
	class Meta:
		model = App
		fields = ['name', 'key_api']
