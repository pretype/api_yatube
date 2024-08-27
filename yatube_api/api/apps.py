"""Модуль с конфигурацией приложения api проекта Api_yatube."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Класс с конфигурацией приложения api."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
