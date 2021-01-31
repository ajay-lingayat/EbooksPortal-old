from .serializers import *
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

class ProfilesViewset(ModelViewSet):
    serializer_class = ProfilesSerializer
    filterset_class = ProfilesFilter
    queryset = Profile.objects.all()

class TagsViewset(ModelViewSet):
    serializer_class = TagsSerializer
    filterset_class = TagsFilter
    queryset = Tag.objects.all()

class SectionsViewset(ModelViewSet):
    serializer_class = SectionsSerializer
    filterset_class = SectionsFilter
    queryset = Section.objects.all()

class AllCountsViewset(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        users = User.objects.all().count()
        books = Book.objects.all().count()
        papers = Paper.objects.all().count()
        book_downloads = sum([book.downloads for book in Book.objects.all()])
        paper_downloads = sum([paper.downloads for paper in Paper.objects.all()])
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