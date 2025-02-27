from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from .models import Book
from django.contrib import messages
from .forms import ExampleForm


# Create your views here.
@login_required
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})


@login_required
@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title").strip()
        author = request.POST.get("author").strip()
        publication_year = request.POST.get("publication_year")

        if not title or not author:
            return render(request, "bookshelf/form_example.html", {"error": "Fields cannot be empty"})
            
        Book.objects.create(title=title, author=author, publication_year=publication_year)
        messages.success(request, "Book created successfully!")
        return redirect("book_list")
    
    return render(request, "bookshelf/form_example.html")


@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.publication_year = request.POST.get("publication_year")
        book.save()
        messages.success(request, "Book updated successfully!")
        return redirect("book_list")
    
    return render(request, "books/book_form.html")

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully!")
        return redirect("book_list")
    
    return render(request, "books/book_confirm_delete.html", {"book": book})

def add_book(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
        
    else:
        form = ExampleForm()

    return render(request, "bookshelf/add_book.html", {"form": form})

