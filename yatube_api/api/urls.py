from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import PostViewSet, CommentViewSet, FollowViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/posts/<int:post_id>/comments/',
         CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='post-comments'),
    path('v1/posts/<int:post_id>/comments/<int:pk>/',
         CommentViewSet.as_view({'get': 'retrieve',
                                 'put': 'update',
                                 'patch': 'partial_update',
                                 'delete': 'destroy'}),
         name='comment-detail'),
    path('v1/jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
