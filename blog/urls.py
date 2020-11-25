from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('about_blogs/', views.about_blogs, name='about_blogs'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('teg/<int:rubric_id>/', views.by_rubric, name='by_rubric'),
    # Из HTML главной страницы мы получили post.rubric.pk который стал
    # <int:rubric_id> , после чего id отправляется в views.by_rubric
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('home/', views.home, name='home'),

]