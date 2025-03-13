from django.shortcuts import render
from rest_framework import generics, permissions, filters
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# Create your views here.

# Creating a list view to retrieve all books.
class ListView(generics.ListAPIView):
    # API view ti retrieve all list of books with filtering, searching, and ordering capabilities.
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Adding filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Define filtering fields 
    filterset_fields = ['title', 'author', 'publiction_yer']

    # Enable searching on specific fields 
    search_fields = ['title']

    # Enable ordering on fields 
    ordering_fields = ['title', 'publication_year']
    ordering = ['title'] # Default ordering by title 

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
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions_classes = [permissions.IsAuthenticated] # Only authenticated users can delete.
