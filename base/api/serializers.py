from django.contrib.auth.models import User, auth

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from base.models import *
from books.api.serializers import BooksSerializer
from papers.api.serializers import PapersSerializer

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

class ProfilesSerializer(ModelSerializer):
    user = UsersSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['id', 'user', 'theme']

class TagsSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class SectionsSerializer(ModelSerializer):
    books = BooksSerializer(many=True, read_only=True)
    papers = PapersSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ('id', 'name', 'category', 'books', 'papers')