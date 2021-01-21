from django.urls import path
from . import views

urlpatterns =[
    path('', views.papers, name='papers'),
    path('all/', views.all, name='all'),
    path('open-portal/<int:paper>/', views.open_portal, name='open_portal'),
    path('download/<int:paper>/', views.download, name='download'),
]