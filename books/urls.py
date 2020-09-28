from django.urls import path
from . import views

urlpatterns =[
    path('', views.query, name='query'),
    path('all', views.all_books, name='all_books'),
    path('open-portal/<int:id_no>', views.open_portal, name='open_portal'),
]