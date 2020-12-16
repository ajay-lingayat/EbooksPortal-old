from django.contrib import admin

from .models import *

from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
class PaperHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['id', 'title', 'downloads', 'create_date']
    history_list_display = ['status']
    search_fields = ['id', 'title', 'downloads']

class PaperSectionHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['id', 'text']
    history_list_display = ['status']
    search_fields = ['id', 'text']

admin.site.register(Paper, PaperHistoryAdmin)
admin.site.register(PaperSection, PaperSectionHistoryAdmin)