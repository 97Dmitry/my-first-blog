from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets
from .models import Post, Comments, Rubric, ValueRatingPost


class PostList(viewsets.ViewSet):
    """Записи на сайте"""
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostListSerializer(post)
        return Response(serializer.data)
    
    # serializer = PostListSerializer(queryset, many=True)
    # return Response(serializer.data)
    # def get(self, request):
    # rubrics = Rubric.objects.all()
    # posts_serialize = PostListSerializer(posts, many=True)
    # tags_serialize = TagsSerializer(rubrics, many=True)
    # return Response({"posts": posts_serialize.data})

    # def current(self, request, pk=None):
    #     queryset = Post.objects.all()
    #     post = get_object_or_404(queryset, pk=pk)
    #     serializer = PostListSerializer(post)
    #     return Response(serializer.data)
    #
    # def create(self, ):
    #     pass


class CommentList(viewsets.ViewSet):
    """Комментарии к записям"""
    def list(self, request):
        queryset = Comments.objects.all()
        serializer = CommentListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Comments.objects.filter(post__exact=pk)
        # comments = get_object_or_404(queryset)
        serializer = CommentListSerializer(queryset, many=True)
        return Response(serializer.data)


class TagsList(viewsets.ViewSet):
    """Категории для записей"""
    def list(self, request):
        """Список всех категорий"""
        queryset = Rubric.objects.all()
        serializer = TagsListSerializer(queryset, many=True)
        return Response(serializer.data)

    def current_tag(self, request, pk=None):
        """Конкретная категория"""
        queryset = Rubric.objects.get(pk=pk)
        serializer = TagsListSerializer(queryset)
        return Response(serializer.data)

    def posts(self, request, pk=None):
        """Список всех записей по категории"""
        queryset = Post.objects.filter(rubric_id=pk)
        serializer = PostListSerializer(queryset, many=True)
        return Response(serializer.data)


class RatingList(viewsets.ViewSet):
    """Рейтинг записи"""
    def cur_list(self, request, id=None):
        queryset = ValueRatingPost.objects.filter(post_id=id)
        serializer = RatingListSerializer(queryset, many=True)
        return Response(serializer.data)
