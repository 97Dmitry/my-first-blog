from rest_framework import serializers
from .models import Post, Rubric, Comments


class TagsListSerializer(serializers.ModelSerializer):
    """Список тегов"""

    class Meta:
        model = Rubric
        fields = ("__all__")


class CommentListSerializer(serializers.ModelSerializer):
    """Комментарии к постам"""

    post = serializers.SlugRelatedField(slug_field="id", read_only=True)

    class Meta:
        model = Comments
        fields = ("post", "name", "email", "comment", "created")


class PostListSerializer(serializers.ModelSerializer):
    """Список постов"""

    rubric = serializers.SlugRelatedField(slug_field="rubric", read_only=True)
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)
    comments = CommentListSerializer(many=True)

    class Meta:
        model = Post
        fields = ("title", "author", "text", "created_date", "rubric", "comments", "id")
