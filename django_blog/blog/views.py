from profile import Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import FormPost, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from taggit.models import Tag

# Create your views here.
class CumstomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

def Register(request):
    if request.method == 'POST':
        form = CumstomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        else:
            messages.error(request, "Your registration failed. Please check your details entered.")
    else:
       form = CumstomUserCreationForm()

    return render(request, "blog/register.html", {"form": form})

def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You are logged in now.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        
    return render(request, "blog/login.html", {"form": form})

def Logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")

@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, "blog/profile.html", {"profile": profile})

# List for all posts
class ListViewPost(ListView):
    model = Post
    templates = 'blog/listing.html'
    context_object_name = 'posts'

# View details of a single post
class DetailViewPost(DetailView):
    model = Post
    templates = 'blog/post_view.html'

# Create a new post
class CreateViewPost(CreateView, LoginRequiredMixin):
    model = Post
    form_class = FormPost 
    templates = 'blog/post_create.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user # Assigns logged in user as author
        return super().form_valid(form)
    
# Update a post (only authors can update)
class UpdateViewPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = FormPost
    templates = 'blog/post_edit.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author # Only author can edit

# Delete a post (only authors can delete a post)
class DeleteViewPost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    templates = 'blog/post_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author # Only author can delete 

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})
  
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = Comment
   template_name = 'blog/delete.html'

   def test_func(self):
       comment = self.get_object()
       return self.request.user == comment.author
   
   def get_success_url(self):
       return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/tagged_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag = get_object_or_404(Tag, slug=self.kwargs.get('tag_slug'))
        return Post.objects.filter(tags__in=[tag])
    
def search_posts(request):
    query = request.GET.get('q')

    if query:
        results = Post.objects.filter(
            title__icontains=query
        ) | Post.objects.filter(
            content__icontains=query
        ) | Post.objects.filter(
            tags__name__icontains=query
        ).distinct()
    
    else:
        result = Post.objects.none()

    return render(request, 'blog/search_results.html', {'results': results, 'query': query})

