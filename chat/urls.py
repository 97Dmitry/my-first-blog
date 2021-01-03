from django.conf.urls import url
from . import views

urlpatterns = [
    url('blog_chat', views.chat, name='chat'),

]
