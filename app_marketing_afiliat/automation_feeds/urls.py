#
#
#
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('promotions/', views.PromotionsPageView.as_view(), name='promotions'),
    path('feeds/', views.FeedsPageView.as_view(), name='feeds'),
    path('shops/', views.ShopsPageView.as_view(), name='shops'),
    path('contact/', views.ContactPageView.as_view(), name="contact"),
    path('succes-contact/', views.SuccesContactForm.as_view(), name="succes-contact"),
]
