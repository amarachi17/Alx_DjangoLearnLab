from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# Create your views here.

# Creating a list view to retrieve all books.
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Creating a detail view to retrieve a single book by its ID.
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
   
# Creating a create view to add a new book.
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions_classes = [permissions.IsAuthenticated] # Only authenticated users can create.

# Creating a update view to modify an existing book.
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions_classes = [permissions.IsAuthenticated] # Only authenticated users can update.

# Creating a delete view to remove a book.
class DeleteView(generics.DestoryAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions_classes = [permissions.IsAuthenticated] # Only authenticated users can delete.
