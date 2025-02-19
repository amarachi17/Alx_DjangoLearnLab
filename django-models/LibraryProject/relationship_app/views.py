from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse
from django.views.generic.detail import DetailView
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
    
# Login view using Django's built-in LoginView
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"
    
# Logout view using Django's built-in LogoutView
class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"
    
# Use Registration View
def register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("home") # Redirect to home after successful registration
    
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})