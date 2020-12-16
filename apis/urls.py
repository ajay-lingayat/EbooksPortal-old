from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users/all', UserViewset, basename='Users')
router.register('users/staff', StaffViewset, basename='Staff Members')
router.register('users/active', ActiveUsersViewset, basename='Active Users')
router.register('users/end', EndUsersViewset, basename='End Users')
router.register('books/all', BooksViewset, basename='Books')
router.register('books/sections', BookSectionsViewset, basename='Book Sections')
router.register('papers/all', PapersViewset, basename='Papers')
router.register('papers/sections', PaperSectionsViewset, basename='Paper Sections')

urlpatterns = [
    path('', include(router.urls)),
    path('count', AllCountsViewset.as_view(), name='All Counts'),
]