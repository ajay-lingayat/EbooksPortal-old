from django.contrib.auth.models import User, auth
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from books.models import *
from papers.models import *

class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_login', 'username', 'is_staff', 'is_superuser',
                  'first_name', 'last_name', 'email', 'is_active', 'date_joined', 'groups',
                  'user_permissions' ]

class StaffSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_login', 'username', 'is_superuser',
                  'first_name', 'last_name', 'email', 'is_active', 'date_joined', 'groups',
                  'user_permissions' ]

class ActiveUsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_login', 'username', 'is_superuser',
                  'first_name', 'last_name', 'email', 'is_staff', 'date_joined', 'groups',
                  'user_permissions' ]

class EndUsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_login', 'username',
                  'first_name', 'last_name', 'email', 'date_joined' ]

class BooksSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookSectionsSerializer(ModelSerializer):
    class Meta:
        model = BookSection
        fields = '__all__'

class PapersSerializer(ModelSerializer):
    class Meta:
        model = Paper
        fields = '__all__'

class PaperSectionsSerializer(ModelSerializer):
    class Meta:
        model = PaperSection
        fields = '__all__'