from django.conf.urls import url
from registration import views

urlpatterns = [
    url('sing_up/', views.sing_up, name='sing_up'),
    url('sing_in/', views.sing_in, name='sing_in'),

]





