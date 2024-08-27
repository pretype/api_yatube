"""Модуль с определением разрешений приложения api проекта Api_yatube."""

from rest_framework import permissions


class IsAuthorPermission(permissions.BasePermission):
    """Класс с проверкой прав пользователя."""

    def has_object_permission(self, request, view, obj):
        """Проверяет доступ текущего пользователя к функциям приложения."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsAuthenticatedUserPermission(permissions.IsAuthenticated):
    """Класс с проверкой прав аутентифицированного пользователя."""
