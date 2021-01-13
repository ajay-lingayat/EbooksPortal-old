from django.contrib import admin

from .models import *

from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
class BookHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['id', 'title', 'create_date', 'downloads']
    history_list_display = ['status']
    search_fields = ['id', 'title', 'downloads']
    readonly_fields = ('downloads', 'create_date')
    list_filter = ['create_date',]
    date_hierarchy = 'create_date'
    filter_horizontal = ('tags',)

class BookSectionHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['id', 'name']
    history_list_display = ['status']
    search_fields = ['id', 'name']
    filter_horizontal = ('books',)

admin.site.register(Book, BookHistoryAdmin)
admin.site.register(BookSection, BookSectionHistoryAdmin)