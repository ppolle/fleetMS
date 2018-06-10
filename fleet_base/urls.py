from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^owner-signup/$',views.ownerSignup,name = 'owner-signup'),
    url(r'^sacco-signup/$',views.saccoSignup,name = 'sacco-signup'),
]
