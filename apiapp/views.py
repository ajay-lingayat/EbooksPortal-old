from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .serializer import *
from .filtersets import *
from books.models import *
from papers.models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class UserViewset(ModelViewSet):
    serializer_class = UsersSerializer
    filterset_class = UserFilter
    queryset = User.objects.all()

class StaffViewset(ModelViewSet):
    serializer_class = StaffSerializer
    filterset_class = StaffFilter
    
    def get_queryset(self):
        queryset = User.objects.filter(is_staff=True)
        return queryset
    
class ActiveUsersViewset(ModelViewSet):
    serializer_class = ActiveUsersSerializer
    filterset_class = ActiveUsersFilter

    def get_queryset(self):
        queryset = User.objects.filter(is_active=True)
        return queryset

class EndUsersViewset(ModelViewSet):
    serializer_class = EndUsersSerializer
    filterset_class = EndUsersFilter

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

class AllCountsViewset(APIView):

    permission_classes = [AllowAny]

    def get(self, request, format=None):
        users = User.objects.all().count()
        books = book.objects.all().count()
        papers = paper.objects.all().count()
        book_downloads = book_download.objects.all().count()
        paper_downloads = paper_download.objects.all().count()
        total_downloads = book_downloads + paper_downloads

        return Response(
            {
                'users': users,
                'books': books,
                'papers': papers,
                'book_downloads': book_downloads,
                'paper_downloads': paper_downloads,
                'total_downloads': total_downloads
            }
        )

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