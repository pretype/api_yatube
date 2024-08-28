"""Модуль с определением сериализаторов приложения api проекта Api_yatube."""

from rest_framework import serializers

from posts.models import Comment, Group, Post


class CommentSerializer(serializers.ModelSerializer):
    """Класс, определяющий сериализатор для комментариев."""

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        """Класс с метаданными модели комментария."""

        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    """Класс, определяющий сериализатор для групп."""

    class Meta:
        """Класс с метаданными модели группы."""

        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Класс, определяющий сериализатор для постов."""

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        """Класс с метаданными модели поста."""

        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        read_only_fields = ('author',)
