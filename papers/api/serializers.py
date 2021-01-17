from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from papers.models import *

class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class PapersSerializer(ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Paper
        fields = ('id', 'title', 'attachment', 'image', 'create_date', 'downloads', 'tags')