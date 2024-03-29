from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin, GroupAdmin

from .resources import *

from allauth.account.admin import EmailAddressAdmin
from rest_framework.authtoken.admin import TokenAdmin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
AdminSite.site_header = 'EbooksPortal administration'
AdminSite.site_title = 'EbooksPortal administration'
AdminSite.enable_nav_sidebar = False

class ProfileAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = ['id', 'user', 'theme']
    list_filter = ['theme']
    history_list_display = ['status']
    search_fields = ['user__username']
    raw_id_fields = ['user']
    resource_class = ProfileResource

class BookInline(admin.TabularInline):
    model = Book.tags.through

class PaperInline(admin.TabularInline):
    model = Paper.tags.through

class TagAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    inlines = [BookInline, PaperInline]
    resource_class = TagResource

class SectionAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = ['id', 'name', 'category', 'no_of_books', 'no_of_papers']
    list_filter = ['category']
    history_list_display = ['status']
    search_fields = ['name']
    filter_horizontal = ('books', 'papers')
    resource_class = SectionResource

    def get_queryset(self, request):
        qs = super(SectionAdmin, self).get_queryset(request)
        qs = qs.annotate(models.Count('books'))
        qs = qs.annotate(models.Count('papers'))
        return qs

    def no_of_books(self, obj):
        return obj.books__count
    no_of_books.admin_order_field = 'books__count'
    
    def no_of_papers(self, obj):
        return obj.papers__count
    no_of_papers.admin_order_field = 'papers__count'

def make_staff_member(modeladmin, request, queryset):
    queryset.update(is_staff=True)
make_staff_member.short_description = "Make selected users as staff members"

def remove_from_staff(modeladmin, request, queryset):
    queryset.update(is_staff=False)
remove_from_staff.short_description = "Demote selected users from staff"

def make_superuser(modeladmin, request, queryset):
    queryset.update(is_superuser=True)
make_superuser.short_description = "Make selected users as superuser"

class CustomUserAdmin(UserAdmin, ImportExportModelAdmin):
    def __init__(self, *args, **kwargs):
        self.empty_value_display = 'NA'
        self.actions = [make_staff_member, remove_from_staff, make_superuser]
        self.list_display = ('id',)+self.list_display
        self.list_display += ('date_joined', 'last_login')
        self.list_filter += ('date_joined', 'last_login')
        self.date_hierarchy = 'date_joined'
        self.resource_class = UserResource
        super(UserAdmin, self).__init__(*args, **kwargs)

def verify_emails(modeladmin, request, queryset):
    queryset.update(verified=True)
verify_emails.short_description = "Verify selected email addresses"

def unverify_emails(modeladmin, request, queryset):
    queryset.update(verified=False)
unverify_emails.short_description = "Unverify selected email addresses"

class CustomEmailAddressAdmin(EmailAddressAdmin, ImportExportModelAdmin):
    def __init__(self, *args, **kwargs):
        self.list_display = ('id',)+self.list_display
        self.actions = [verify_emails, unverify_emails]
        self.empty_value_display = 'NA'
        self.resource_class = EmailAddressResource
        super(EmailAddressAdmin, self).__init__(*args, **kwargs)
        
class CustomGroupAdmin(GroupAdmin, ImportExportModelAdmin):
    def __init__(self, *args, **kwargs):
        self.list_display = ('id',)+self.list_display
        self.resource_class = GroupResource
        super(GroupAdmin, self).__init__(*args, **kwargs)

TokenAdmin.list_display = ('pk',)+TokenAdmin.list_display
TokenAdmin.search_fields = ['key', 'user__username']
TokenAdmin.raw_id_fields = ['user']
TokenAdmin.list_filter = ['created']
TokenAdmin.date_hierarchy = 'created'

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(EmailAddress)
admin.site.register(EmailAddress, CustomEmailAddressAdmin)
admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)