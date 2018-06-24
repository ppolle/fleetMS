from django.conf.urls import url

from . import views
app_name = 'sup'

urlpatterns = [
url(r'^$', views.home, name='dashboard'),
url(r'^profile$',views.profile,name='profile'),
url(r'^editSupervisor/$',views.editSupervisor,name = 'editSupervisor'),

url(r'^createDriver/$',views.createDriver,name = 'createDriver'),
url(r'^editDriver/(\d+)',views.editDriver,name = 'editDriver'),
url(r'^drivers/$',views.allDrivers,name = 'allDrivers'),
url(r'^deleteDriver/(\d+)$',views.deleteDriver,name = 'deleteDriver'),

url(r'^createConductor/$',views.createConductor,name = 'createConductor'),
url(r'^editConductor/(\d+)$',views.editConductor,name = 'editConductor'),
url(r'^conductors/$',views.allConductors,name = 'allConductors'),
url(r'^deleteConductor/(\d+)$',views.deleteConductor,name = 'deleteConductor'),
]
