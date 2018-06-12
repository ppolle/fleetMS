from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login),
    url(r'^$', views.home, name='home'),
    url(r'^select-sigup/$', views.select, name='select'),
    url(r'^owner-signup/$', views.ownerSignup, name='owner-signup'),
    url(r'^sacco-signup/$', views.saccoSignup, name='sacco-signup'),
    url(r'^user-logout/$', views.logout, name='logout'),
    url(r'^login/$', views.login, name='login'),
    url(r'^loginViews/$', views.loginViews, name='loginViews'),
]
