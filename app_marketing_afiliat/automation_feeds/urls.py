#
#
#
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('promotions/', views.promotions, name='promotions'),
    path('feeds/', views.feeds, name='feeds'),
    path('shops/', views.shops, name='shops'),
]
