from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from books.models import *

class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class BooksSerializer(ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'attachment', 'image', 'create_date', 'downloads', 'tags')