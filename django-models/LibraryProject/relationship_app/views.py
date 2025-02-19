from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book 
from .models import Library

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books":books})
    # book_list = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    # return HttpResponse(book_list, content_type = "text/plain")

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
    