from import_export import resources
from .models import *

class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        fields = ('id', 'title', 'attachment', 'image', 'tags', 'create_date', 'downloads')