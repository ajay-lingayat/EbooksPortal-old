from django.contrib import admin

from .resources import *

from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class BookHistoryAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = ['id', 'title', 'create_date', 'downloads']
    history_list_display = ['status']
    search_fields = ['id', 'title', 'downloads']
    readonly_fields = ('downloads', 'create_date')
    list_filter = ['create_date',]
    date_hierarchy = 'create_date'
    filter_horizontal = ('tags',)
    resource_class = BookResource

admin.site.register(Book, BookHistoryAdmin)