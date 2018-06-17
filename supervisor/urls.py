from django.conf.urls import url

from . import views
app_name = 'sup'

urlpatterns = [
url(r'^$', views.home, name='dashboard'),
url(r'^editSupervisor$',views.editSupervisor,name = 'editSupervisor'),
url(r'^createDriver$',views.createDriver,name = 'createDriver'),
]
