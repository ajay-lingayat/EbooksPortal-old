import  django_filters
from django_filters import rest_framework
from books.models import *
from papers.models import *
from django.contrib.auth.models import User, auth

class UserFilter(rest_framework.FilterSet):
    class Meta:
        model = User
        fields = {
            'id': ['in'],
            'username': ['icontains'],
            'is_staff': ['icontains'],
            'is_active': ['icontains'],
            'is_superuser': ['icontains'],
            'first_name': ['icontains'],
            'last_name': ['icontains']
        }

class StaffFilter(rest_framework.FilterSet):
    class Meta:
        model = User
        fields = {
            'id': ['in'],
            'username': ['icontains'],
            'is_active': ['icontains'],
            'is_superuser': ['icontains'],
            'first_name': ['icontains'],
            'last_name': ['icontains']
        }

class ActiveUsersFilter(rest_framework.FilterSet):
    class Meta:
        model = User
        fields = {
            'id': ['in'],
            'username': ['icontains'],
            'is_superuser': ['icontains'],
            'first_name': ['icontains'],
            'last_name': ['icontains']
        }

class EndUsersFilter(rest_framework.FilterSet):
    class Meta:
        model = User
        fields = {
            'id': ['in'],
            'username': ['icontains'],
            'first_name': ['icontains'],
            'last_name': ['icontains']
        }

class BooksFilter(rest_framework.FilterSet):
    class Meta:
        model = book
        fields = {
            'id': ['in'],
            'title': ['icontains']
        }

class BookDownloadsFilter(rest_framework.FilterSet):
    book_title = rest_framework.CharFilter(field_name='book__title', lookup_expr='icontains')

    class Meta:
        model = book_download
        fields = {
            'id': ['in'],
            'book': ['in']
        }

class BookSectionsFilter(rest_framework.FilterSet):
    class Meta:
        model = book_section
        fields = {
            'id': ['in']
        }

class PapersFilter(rest_framework.FilterSet):
    class Meta:
        model = paper
        fields = {
            'id': ['in'],
            'title': ['icontains']
        }

class PaperDownloadsFilter(rest_framework.FilterSet):
    paper_title = rest_framework.CharFilter(field_name='paper__title', lookup_expr='icontains')
    
    class Meta:
        model = paper_download
        fields = {
            'id': ['in'],
            'paper': ['in']
        }

class PaperSectionsFilter(rest_framework.FilterSet):
    class Meta:
        model = paper_section
        fields = {
            'id': ['in']
        }