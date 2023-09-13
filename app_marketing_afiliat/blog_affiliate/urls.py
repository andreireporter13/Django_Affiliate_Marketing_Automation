#
#
#
from django.urls import path
from . import views
#
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.BlogPageView.as_view(), name="blog"),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]

# for media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
