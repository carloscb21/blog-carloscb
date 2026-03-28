from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from blog.models import Post, Category, Tag
from projects.models import Project
from .serializers import PostSerializer, CategorySerializer, TagSerializer, ProjectSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.filter(active=True).order_by('order')
    serializer_class = ProjectSerializer
    lookup_field = 'slug'

class PostViewSet(viewsets.ModelViewSet):
    """
    Permite lectura global, pero restringe mutaciones a usuarios autenticados.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    @action(detail=True, methods=['post'], permission_classes=[permissions.AllowAny])
    def like(self, request, slug=None):
        post = self.get_object()
        post.likes += 1
        post.save(update_fields=['likes'])
        return Response({'status': 'like_incrementado', 'likes': post.likes})
