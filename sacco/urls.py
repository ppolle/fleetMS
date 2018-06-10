from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.dashboard, name='sacco_home'),
    # url(r'^new/sacco/$', views.sacco, name='register_sacco'),
    url(r'^new/supervisor/$', views.superlist, name='supervisor'),
    url(r'^profile/(?P<profile_id>[-\w]+)/$', views.profile, name='profile'),
    url(r'^edit/$', views.edit_profile, name='edit'),
        
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
