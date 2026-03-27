from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import CategoryViewSet, TagViewSet, ProjectViewSet, PostViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'posts', PostViewSet, basename='post')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
]
