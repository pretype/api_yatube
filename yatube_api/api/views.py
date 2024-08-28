"""Модуль с вьюсетами приложения api проекта Api_yatube."""

from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .permission import IsAuthenticatedUserPermission, IsAuthorPermission
from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post


def get_post_or_404(self):
    """Отдаёт определенный пост или ошибку 404."""
    return get_object_or_404(Post, id=self.kwargs.get('post_id'))


class PostViewSet(viewsets.ModelViewSet):
    """Класс с определением представления поста."""

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthorPermission, IsAuthenticatedUserPermission)

    def perform_create(self, serializer):
        """Записывает в БД текущего пользователя автором поста."""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Класс с определением представления комментариев."""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthorPermission, IsAuthenticatedUserPermission)

    def get_queryset(self):
        """Переопределяет метод, для фильтрования комментариев."""
        return get_post_or_404(self).comments.all()

    def perform_create(self, serializer):
        """Записывает в БД пост и текущего пользователя автором комментария."""
        serializer.save(author=self.request.user, post=get_post_or_404(self))


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Класс с определением представления группы."""

    serializer_class = GroupSerializer
    queryset = Group.objects.all()
