"""Модуль с вьюсетами приложения api проекта Api_yatube."""

from http import HTTPStatus

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .permission import IsAuthenticatedUserPermission, IsAuthorPermission
from .serializers import (CommentSerializer, GroupSerializer, PostSerializer,
                          UserSerializer)
from posts.models import Comment, Group, Post, User


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Класс с определением представления пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    """Класс с определением представления поста."""

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthorPermission, IsAuthenticatedUserPermission]

    def perform_create(self, serializer):
        """Записывает в БД текущего пользователя автором поста."""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Класс с определением представления комментариев."""

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthorPermission, IsAuthenticatedUserPermission]

    def get_queryset(self):
        """Переопределяет метод, для фильтрования комментариев."""
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return post.comments

    def perform_create(self, serializer):
        """Записывает в БД пост и текущего пользователя автором комментария."""
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ModelViewSet):
    """Класс с определением представления группы."""

    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    def create(self, request):
        """Перехватывает попытку создания группы через API."""
        return Response(status=HTTPStatus.METHOD_NOT_ALLOWED)
