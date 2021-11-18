from rest_framework import serializers
from .models import Author, ToDoItem

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify which model to use and
        # the specific fields on it we want to expose:
        fields = (
            'id', # created automatically by Django! (Not present in Author model)
            'name',
            'email',
        )
        model = Author

class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'dateOfCreation',
            'deadline',
            'author',
        )
        model = ToDoItem