from django.urls import path
from . import views

urlpatterns = [
    path('first', views.first_page),
    path('second', views.second_page),
    path('shop', views.shop),
    path('example', views.example),
    path('', views.landing_page)
]
