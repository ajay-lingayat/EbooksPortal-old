from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books/all', BooksViewset, basename='Books')

urlpatterns = [
    path('', include(router.urls)),
]