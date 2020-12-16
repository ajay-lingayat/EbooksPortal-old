import  django_filters
from django_filters import rest_framework
from books.models import *
from papers.models import *
from django.contrib.auth.models import User, auth

class UserFilter(rest_framework.FilterSet):
    class Meta:
        model = User
        fields = {
            'id': ['exact'],
            'username': ['icontains'],
            'is_staff': ['exact'],
            'is_active': ['exact'],
            'is_superuser': ['exact'],
            'first_name': ['icontains'],
            'last_name': ['icontains']
        }

class StaffFilter(rest_framework.FilterSet):
    class Meta:
        model = User
        fields = {
            'id': ['exact'],
            'username': ['icontains'],
            'is_active': ['exact'],
            'is_superuser': ['exact'],
            'first_name': ['icontains'],
            'last_name': ['icontains']
        }

class ActiveUsersFilter(rest_framework.FilterSet):
    class Meta:
        model = User
        fields = {
            'id': ['exact'],
            'username': ['icontains'],
            'is_superuser': ['exact'],
            'first_name': ['icontains'],
            'last_name': ['icontains']
        }

class EndUsersFilter(rest_framework.FilterSet):
    class Meta:
        model = User
        fields = {
            'id': ['exact'],
            'username': ['icontains'],
            'first_name': ['icontains'],
            'last_name': ['icontains']
        }

class BooksFilter(rest_framework.FilterSet):
    class Meta:
        model = Book
        fields = {
            'id': ['exact'],
            'title': ['icontains'],
            'downloads': ['exact', 'lte', 'gte']
        }

class BookSectionsFilter(rest_framework.FilterSet):
    class Meta:
        model = BookSection
        fields = {
            'id': ['exact']
        }

class PapersFilter(rest_framework.FilterSet):
    class Meta:
        model = Paper
        fields = {
            'id': ['exact'],
            'title': ['icontains'],
            'downloads': ['exact', 'lte', 'gte']
        }

class PaperSectionsFilter(rest_framework.FilterSet):
    class Meta:
        model = PaperSection
        fields = {
            'id': ['exact']
        }