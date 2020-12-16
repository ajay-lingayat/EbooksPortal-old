from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('profile', views.profile, name='profile'),
    path('null', views.null, name='null'),
]