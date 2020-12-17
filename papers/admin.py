from django.contrib import admin

from .models import *

from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
class PaperHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['id', 'title', 'create_date', 'downloads']
    history_list_display = ['status']
    search_fields = ['id', 'title', 'downloads']
    readonly_fields=('downloads', 'create_date')
    list_filter = ['create_date',]

class PaperSectionHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['id', 'text']
    history_list_display = ['status']
    search_fields = ['id', 'text']

admin.site.register(Paper, PaperHistoryAdmin)
admin.site.register(PaperSection, PaperSectionHistoryAdmin)