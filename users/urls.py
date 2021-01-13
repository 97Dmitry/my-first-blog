from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'api/profile_list', views.ProfileSerializer, basename='rest_profile_list')


urlpatterns = [
    path('sing_up/', views.sing_up, name='sing_up'),
    path('sing_in/', views.sing_in, name='sing_in'),
    path('logout/', views.logout_user, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('user_page/', views.user_page, name='user_page'),
    path('recovery_password/', views.PasswordRecovery.as_view(), name='recovery_password'),
    path('password_recovery_done', views.PasswordRecoveryDone.as_view(), name='password_recovery_done'),
    path('recovery_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        views.PasswordRecoveryConfirm.as_view(), name='recovery_confirm'),
    path('recovery_complete/', views.PasswordRecoverComplete.as_view(), name='recovery_complete'),

] + router.urls
