from import_export import resources
from .models import *

class PaperResource(resources.ModelResource):
    class Meta:
        model = Paper
        fields = ('id', 'title', 'attachment', 'image', 'tags', 'create_date', 'downloads')