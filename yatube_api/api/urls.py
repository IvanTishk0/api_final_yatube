from django.urls import include
from django.urls import path
from rest_framework import routers
from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='post-comments'
)
router.register(
    r'follow',
    FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/jwt/create/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
