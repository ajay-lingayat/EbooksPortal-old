from django.urls import path

from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('all/', views.all, name='all'),
    path('open-portal/<int:book>/', views.open_portal, name='open_portal'),
    path('download/<int:book>/', views.download, name='download'),
]