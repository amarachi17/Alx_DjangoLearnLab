from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializer import BookSerializer

# Create your views here.
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
