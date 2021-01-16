from rest_framework.serializers import ModelSerializer
from papers.models import *

class PapersSerializer(ModelSerializer):
    class Meta:
        model = Paper
        fields = '__all__'