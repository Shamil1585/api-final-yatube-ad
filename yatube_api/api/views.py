from rest_framework import viewsets, permissions, mixins
from rest_framework import filters

from posts.models import Post, Comment, Follow, Group
from .serializers import (
    PostSerializer,
    CommentSerializer,
    FollowSerializer,
    GroupSerializer
)
from .permissions import IsAuthorOrReadOnly


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = None


class PostViewSet(viewsets.ModelViewSet):
    # Сортировка по id (старые первыми)
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    # Сортировка по id (старые первыми)
    queryset = Comment.objects.all().order_by('id')
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = None

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        if post_id:
            return self.queryset.filter(post_id=post_id)
        return self.queryset.none()

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(
            author=self.request.user,
            post_id=post_id
        )


class FollowViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    pagination_class = None

    def get_queryset(self):
        return Follow.objects.filter(
            user=self.request.user
        ).select_related('following')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
