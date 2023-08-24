#
#
#
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('automation_feeds.urls')),
    path('blog/', include('blog_affiliate.urls')),
    re_path(r'^static/(?P<path>.)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    re_path(r'^media/(?P<path>.)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
