from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'owner'

urlpatterns=[
        
    url('^$', views.home, name = 'home'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^new/vehicle/$', views.vehicle, name='createVehicle'),
    url(r'^editVehicle/(\d+)', views.editVehicle, name='editVehicle'),
    url(r'^deleteVehicle/(\d+)',
        views.deleteVehicle, name='deleteVehicle'),
    url(r'^editProfile/(\d+)', views.editProfile, name='editProfile'),
    url(r'^crewDetails/(\d+)', views.crewDetails,  name='crewDetails'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
