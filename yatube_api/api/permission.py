"""Модуль с определением разрешений приложения api проекта Api_yatube."""

from rest_framework import permissions


class IsAuthorPermission(permissions.BasePermission):
    """Класс с проверкой прав пользователя."""

    def has_object_permission(self, request, view, user_content_obj):
        """Проверяет доступ текущего пользователя к функциям приложения."""
        return bool(
            request.method in permissions.SAFE_METHODS
        ) or (
            user_content_obj.author == request.user
        )


class IsAuthenticatedUserPermission(permissions.IsAuthenticated):
    """Класс с проверкой прав аутентифицированного пользователя."""
