from django.urls import path
from . import views

urlpatterns = [
    path('blog_chat/', views.chat, name='chat'),
    path('chat/<str:room_name>/', views.room, name='room'),

]
