from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """Список тегов"""
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    user_rank = serializers.SlugRelatedField(slug_field="rank", read_only=True, many=True)

    class Meta:
        model = Profile
        fields = ("user", "picture", "user_rank")