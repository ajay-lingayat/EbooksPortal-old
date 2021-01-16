import  django_filters
from django_filters import rest_framework
from books.models import *

class BooksFilter(rest_framework.FilterSet):
    class Meta:
        model = Book
        fields = {
            'id': ['exact'],
            'title': ['icontains'],
            'downloads': ['exact', 'lte', 'gte']
        }