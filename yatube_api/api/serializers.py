"""Модуль с определением сериализаторов приложения api проекта Api_yatube."""

from rest_framework import serializers

from posts.models import Comment, Group, Post, User


class CommentSerializer(serializers.ModelSerializer):
    """Класс, определяющий сериализатор для комментариев."""

    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        """Класс с метаданными модели комментария."""

        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post')


class GroupSerializer(serializers.ModelSerializer):
    """Класс, определяющий сериализатор для групп."""

    class Meta:
        """Класс с метаданными модели группы."""

        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Класс, определяющий сериализатор для постов."""

    group = GroupSerializer(read_only=True, required=False)
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        """Класс с метаданными модели поста."""

        model = Post
        fields = '__all__'
        read_only_fields = ('author',)


class UserSerializer(serializers.ModelSerializer):
    """Класс, определяющий сериализатор для пользователей."""

    posts = PostSerializer(many=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        """Класс с метаданными модели пользователя."""

        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name', 'date_joined', 'email')
