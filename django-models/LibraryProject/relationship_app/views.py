from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book 
from .models import Library
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

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
class LoginView(LoginView):
    template_name = "relationship_app/login.html"
    
# Logout view using Django's built-in LogoutView
class LogoutView(LogoutView):
    template_name = "relationship_app/logout.html"
    
# Use Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        # return redirect("home") # Redirect to home after successful registration
    
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# Role check function
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == "Admin"

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == "Librarian"

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == "Member"

# Views for each role
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")