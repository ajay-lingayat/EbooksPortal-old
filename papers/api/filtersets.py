import  django_filters
from django_filters import rest_framework
from papers.models import *

class PapersFilter(rest_framework.FilterSet):
    class Meta:
        model = Paper
        fields = {
            'id': ['exact'],
            'title': ['icontains'],
            'downloads': ['exact', 'lte', 'gte']
        }