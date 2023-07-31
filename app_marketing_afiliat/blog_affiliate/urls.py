#
#
#
from django.urls import path
from . import views


urlpatterns = [
    path('', views.BlogPageView.as_view(), name="blog"),
]
