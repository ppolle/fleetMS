from django.conf.urls import url

from . import views
app_name = 'sup'

urlpatterns = [
url(r'^$', views.home, name='dashboard'),
url(r'^profile$',views.profile,name='profile'),
url(r'^editSupervisor/$',views.editSupervisor,name = 'editSupervisor'),
url(r'^allMatatus/$',views.allMatatus,name = 'allMatatus'),
url(r'^allOwners/$',views.allOwners,name = 'allOwners'),
url(r'^singleMatatu/(\d+)',views.singleMatatu,name = 'singleMatatu'),
url(r'^assignCrew/(\d+)',views.assignCrew,name = 'assignCrew'),
url(r'^deleteCrew/(\d+)',views.deleteCrew,name = 'deleteCrew'),
url(r'^singleOwner/(\d+)',views.singleOwner,name= 'singleOwner'),

url(r'^createDriver/$',views.createDriver,name = 'createDriver'),
url(r'^editDriver/(\d+)',views.editDriver,name = 'editDriver'),
url(r'^drivers/$',views.allDrivers,name = 'allDrivers'),
url(r'^deleteDriver/(\d+)$',views.deleteDriver,name = 'deleteDriver'),

url(r'^createConductor/$',views.createConductor,name = 'createConductor'),
url(r'^editConductor/(\d+)$',views.editConductor,name = 'editConductor'),
url(r'^conductors/$',views.allConductors,name = 'allConductors'),
url(r'^deleteConductor/(\d+)$',views.deleteConductor,name = 'deleteConductor'),
url(r'^issues/$', views.create_issue, name='issuessss')
]
