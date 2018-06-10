from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login),
    url(r'^$', views.home, name='home'),

]
