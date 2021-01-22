from import_export import resources
from .models import *
from allauth.account.models import EmailAddress

class TagResource(resources.ModelResource):
    class Meta:
        model = Tag
        fields = ('id', 'name')

class SectionResource(resources.ModelResource):
    class Meta:
        model = Section
        fields = ('id', 'name', 'books', 'papers', 'category')

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active', 
                'is_staff', 'is_superuser', 'groups', 'user_permissions', 'last_login', 'date_joined')

class EmailAddressResource(resources.ModelResource):
    class Meta:
        model = EmailAddress
        fields = ('id', 'user', 'email', 'verified', 'primary')

class GroupResource(resources.ModelResource):
    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')