from django.conf.urls import url
from users import views

urlpatterns = [
    url('sing_up/', views.sing_up, name='sing_up'),
    url('sing_in/', views.sing_in, name='sing_in'),
    url('logout/', views.logout_user, name='logout'),
    url('change_password/', views.change_password, name='change_password'),
    url('user_page', views.user_page, name='user_page')

]
