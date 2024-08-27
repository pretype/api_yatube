"""Модуль с маршрутизацией приложения api проекта Api_yatube."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = DefaultRouter()

router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/?comments/?',
                CommentViewSet, basename='comment')
router.register('groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
