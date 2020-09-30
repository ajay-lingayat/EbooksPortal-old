from django.contrib.auth.models import User, auth
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from books.models import *
from papers.models import *

class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class StaffSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password', 'last_login', 'username', 'is_superuser',
                  'first_name', 'last_name', 'email', 'is_active', 'date_joined', 'groups',
                  'user_permissions' ]

class ActiveUsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password', 'last_login', 'username', 'is_superuser',
                  'first_name', 'last_name', 'email', 'is_staff', 'date_joined', 'groups',
                  'user_permissions' ]

class EndUsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password', 'last_login', 'username',
                  'first_name', 'last_name', 'email', 'date_joined' ]

class BooksSerializer(ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'

class BookDownloadsSerializer(ModelSerializer):
    class Meta:
        model = book_download
        fields = '__all__'

class BookSectionsSerializer(ModelSerializer):
    class Meta:
        model = book_section
        fields = '__all__'

class PapersSerializer(ModelSerializer):
    class Meta:
        model = paper
        fields = '__all__'

class PaperDownloadsSerializer(ModelSerializer):
    class Meta:
        model = paper_download
        fields = '__all__'

class PaperSectionsSerializer(ModelSerializer):
    class Meta:
        model = paper_section
        fields = '__all__'