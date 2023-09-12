#
#
#
from django.urls import path
from . import views


urlpatterns = [
    path('', views.BlogPageView.as_view(), name="blog"),
    path('<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
]
