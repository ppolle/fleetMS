from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='sacco'

urlpatterns = [
    url(r'^$', views.dashboard, name='sacco_home'),
    url(r'^new/supervisor/$', views.superlist, name='supervisor'),
    url(r'^editSupervisor/(\d+)', views.edit_superlist, name='editSupervisor'),
    url(r'^delete_supervisor/(\d+)', views.delete_supervisor, name='deleteSupervisor'),
    
    
    url(r'^profile/(?P<profile_id>[-\w]+)/$', views.profile, name='profile'),
    url(r'^editSacco/(\d+)', views.edit_profile, name='edit'),
    url(r'^delete_sacco/(\d+)', views.delete_sacco, name='deleteSacco'),
        
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
