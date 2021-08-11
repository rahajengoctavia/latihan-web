from django.urls import path
from . import views

urlpatterns = [
    path ('home', views.home),
    path('first', views.first_page),
    path('second', views.second_page),
    path('allproducts', views.makeover),
    path('shop', views.shop),
    path('example', views.example),
    path('', views.landing_page)
]
