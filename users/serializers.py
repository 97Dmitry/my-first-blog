from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """Список тегов"""
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    user_rank = serializers.SlugRelatedField(slug_field="rank", read_only=True, many=True)

    class Meta:
        model = Profile
        fields = ("user", "picture", "user_rank")


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "email",)