from .serializers import *
from .filtersets import *
from papers.models import *
from rest_framework.viewsets import ModelViewSet

class PapersViewset(ModelViewSet):
    serializer_class = PapersSerializer
    filterset_class = PapersFilter
    queryset = Paper.objects.all()