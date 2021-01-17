from django.urls import path
from . import views

urlpatterns =[
    path('', views.text, name='book_text'),
    path('q/<str:query>', views.query, name='book_query'),
    path('all', views.all_books, name='all_books'),
    path('open-portal/<int:id_no>', views.open_portal, name='book_open_portal'),
    path('mark-download', views.mark_download, name='book_mark_download'),
]