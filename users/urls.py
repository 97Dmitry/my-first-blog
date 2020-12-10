from django.conf.urls import url
from users import views

urlpatterns = [
    url('sing_up/', views.sing_up, name='sing_up'),
    url('sing_in/', views.sing_in, name='sing_in'),
    url('logout/', views.logout_user, name='logout'),
    url('change_password/', views.change_password, name='change_password'),
    url('user_page/', views.user_page, name='user_page'),
    url('recovery_password/', views.PasswordRecovery.as_view(), name='recovery_password'),
    url('password_recovery_done', views.PasswordRecoveryDone.as_view(), name='password_recovery_done'),
    url('recovery_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', views.PasswordRecoveryConfirm.as_view(), name='recovery_confirm'),

]
