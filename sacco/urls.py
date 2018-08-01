from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='sacco'

urlpatterns = [
    url(r'^$', views.dashboard, name='sacco_home'),
    url(r'^new/supervisor/$', views.superlist, name='createSupervisor'),
    url(r'^editSupervisor/(\d+)', views.edit_superlist, name='editSupervisor'),
    url(r'^delete_supervisor/(\d+)', views.delete_supervisor, name='deleteSupervisor'),
    url(r'^fleet/$', views.saccoFleet, name='fleet'),
    url(r'^members/$', views.saccoMembers, name='members'),
    url(r'^supervisors/$', views.saccoSupervisors, name='supervisors'),
    
    url(r'^ownerdetails/(\d+)', views.owner_details, name='ownerDetails'),

    url(r'^profile/$', views.profile, name='profile'),
    url(r'^editSacco/(\d+)', views.edit_profile, name='edit'),
    url(r'^delete_sacco/(\d+)', views.delete_sacco, name='deleteSacco'),
        
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
