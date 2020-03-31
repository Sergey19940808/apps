from django.db import models


class App(models.Model):
	name = models.CharField(max_length=200, verbose_name='Имя приложения')
	key_api = models.CharField(max_length=200, verbose_name='Ключ для авторизации к приложению')
