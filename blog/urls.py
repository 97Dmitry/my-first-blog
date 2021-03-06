from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from . import api


router = DefaultRouter()

router.register(r'api/posts_list', api.PostList, basename='rest_post_list')
router.register(r'api/comments_list', api.CommentList, basename='rest_comment_list')
#router.register(r'api/comment_list', views.CommentList, basename='rest_comment_list')
router.register(r'api/tags_list', api.TagsList, basename='rest_tags_list')
# router.register(r'api/rating_list', views.RatingList, basename='rest_tage_list')

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('about_blogs/', views.about_blogs, name='about_blogs'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # Из HTML главной страницы мы получили post.rubric.pk который стал
    # <int:rubric_id> , после чего id отправляется в views.by_rubric
    path('teg/<int:rubric_id>/', views.by_rubric, name='by_rubric'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('home/', views.home, name='home'),
    path('add_rating/<int:pk>', views.add_rating, name='add_rating'),


    # For REST need use 'api/...'
    # path('api/post_list', views.PostList.as_view({'get': 'list'})),
    # path('api/comment_list/', api.CommentList.as_view({'get': 'list'})),
    # path('api/comment_list/<int:id>/', api.CommentList.as_view({'get': 'retrieve'})),
    path('api/cur_rating/<int:id>/', api.RatingList.as_view({'get': 'cur_list'})),
    path('api/tag_posts/<int:pk>/', api.TagsList.as_view({'get': 'posts'})),
    path('api/post_create/', api.PostCreate.as_view()),


] + router.urls


