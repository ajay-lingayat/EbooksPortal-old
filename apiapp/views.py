from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .serializer import *
from .filtersets import *
from books.models import *
from papers.models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

# Create your views here.
class UserViewset(ModelViewSet):
    serializer_class = UsersSerializer
    filterset_class = UserFilter
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]

class StaffViewset(ModelViewSet):
    serializer_class = StaffSerializer
    filterset_class = StaffFilter
    permission_classes = [IsAdminUser]
    
    def get_queryset(self):
        queryset = User.objects.filter(is_staff=True)
        return queryset
    
class ActiveUsersViewset(ModelViewSet):
    serializer_class = ActiveUsersSerializer
    filterset_class = ActiveUsersFilter
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = User.objects.filter(is_active=True)
        return queryset

class EndUsersViewset(ModelViewSet):
    serializer_class = EndUsersSerializer
    filterset_class = EndUsersFilter
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = User.objects.filter(is_staff=False)
        return queryset

class BooksViewset(ModelViewSet):
    serializer_class = BooksSerializer
    filterset_class = BooksFilter
    queryset = book.objects.all()

class BookDownloadsViewset(ModelViewSet):
    serializer_class = BookDownloadsSerializer
    filterset_class= BookDownloadsFilter
    queryset = book_download.objects.all()

class BookSectionsViewset(ModelViewSet):
    serializer_class = BookSectionsSerializer
    filterset_class = BookSectionsFilter
    queryset = book_section.objects.all()


class PapersViewset(ModelViewSet):
    serializer_class = PapersSerializer
    filterset_class = PapersFilter
    queryset = paper.objects.all()

class PaperDownloadsViewset(ModelViewSet):
    serializer_class = PaperDownloadsSerializer
    filterset_class = PaperDownloadsFilter
    queryset = paper_download.objects.all()

class PaperSectionsViewset(ModelViewSet):
    serializer_class = PaperSectionsSerializer
    filterset_class = PaperSectionsFilter
    queryset = paper_section.objects.all()