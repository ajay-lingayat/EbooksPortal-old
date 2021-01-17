from django.urls import path
from . import views

urlpatterns =[
    path('', views.text, name='paper_text'),
    path('q/<str:query>', views.query, name='paper_query'),
    path('all', views.all_papers, name='all_papers'),
    path('open-portal/<int:id_no>', views.open_portal, name='paper_open_portal'),
    path('mark-download', views.mark_download, name='paper_mark_download'),
]