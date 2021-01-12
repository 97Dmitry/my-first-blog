from rest_framework import serializers
from .models import Post, Rubric

class PostListSerializer(serializers.ModelSerializer):
    """Список постов"""
    # title = serializers.CharField()
    # text = serializers.CharField()

    class Meta:
        model = Post
        fields = ("__all__")


class TagsSerializer(serializers.ModelSerializer):
    """Список тегов"""

    class Meta:
        model = Rubric
        fields = ("__all__")