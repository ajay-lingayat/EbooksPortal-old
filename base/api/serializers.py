from django.contrib.auth.models import User, auth
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from base.models import *

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

class TagsSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class SectionsSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'