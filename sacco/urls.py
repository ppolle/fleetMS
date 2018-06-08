from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='sacco_home'),
    url(r'^new/sacco/$', views.sacco, name='register_sacco'),
    
]
