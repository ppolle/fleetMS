from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^select-sigup/$',views.select,name='select'),
    url(r'^owner-signup/$',views.ownerSignup,name = 'owner-signup'),
    url(r'^sacco-signup/$',views.saccoSignup,name = 'sacco-signup'),
    url(r'^user-logout/$',views.logout,name = 'logout')
]
