from rest_framework import serializers
from blog.models import Post, Category, Tag
from projects.models import Project

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

class PostSerializer(serializers.ModelSerializer):
    # Inclusiones detalladas para modo lectura
    category_detail = CategorySerializer(source='category', read_only=True)
    tags_detail = TagSerializer(source='tags', many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'body', 'excerpt', 'meta_description', 
            'status', 'featured', 'likes', 'created_at', 'updated_at', 
            'published_at', 'category', 'tags', 'category_detail', 'tags_detail'
        ]
        read_only_fields = ['id', 'slug', 'likes', 'created_at', 'updated_at']

class ProjectSerializer(serializers.ModelSerializer):
    tags_detail = TagSerializer(source='tags', many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'description', 'url', 'repo_url', 
            'tags', 'tags_detail', 'order', 'active'
        ]
        read_only_fields = ['id', 'slug']
