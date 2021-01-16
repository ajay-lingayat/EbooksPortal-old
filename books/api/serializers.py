from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from books.models import *

class BooksSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'