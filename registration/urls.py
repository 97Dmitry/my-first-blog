from django.conf.urls import url
from registration import views

urlpatterns = [
    url('sing_up/', views.sing_up, name='sing_up'),

]





