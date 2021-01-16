from .serializers import *
from .filtersets import *
from books.models import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class BooksViewset(ModelViewSet):
    serializer_class = BooksSerializer
    filterset_class = BooksFilter
    queryset = Book.objects.all()