from django.shortcuts import render
from rest_framework import generics
from .models import Author, ToDoItem
from .serializers import AuthorSerializer, ToDoItemSerializer

# Create your views here.

class ListAuthor(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class DetailAuthor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ListToDoItem(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

class DetailToDoItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
