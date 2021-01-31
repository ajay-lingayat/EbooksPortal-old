import  django_filters
from django_filters import rest_framework
from base.models import *

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

class ProfilesFilter(rest_framework.FilterSet):
    user = rest_framework.NumberFilter(field_name='user__id', lookup_expr='exact')
    class Meta:
        model = Profile
        fields = {
            'id': ['exact'],
            'theme': ['exact']
        }

class TagsFilter(rest_framework.FilterSet):
    class Meta:
        model = Tag
        fields = {
            'id': ['exact'],
            'name': ['exact']
        }

class SectionsFilter(rest_framework.FilterSet):
    class Meta:
        model = Section
        fields = {
            'id': ['exact'],
            'name': ['exact'],
            'category': ['exact']
        }