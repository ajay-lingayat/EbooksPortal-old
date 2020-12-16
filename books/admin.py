from django.contrib import admin

from .models import *

from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
class BookHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['id', 'title', 'downloads']
    history_list_display = ['status']
    search_fields = ['id', 'title', 'downloads']

class BookSectionHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['id', 'text']
    history_list_display = ['status']
    search_fields = ['id', 'text']

admin.site.register(Book, BookHistoryAdmin)
admin.site.register(BookSection, BookSectionHistoryAdmin)