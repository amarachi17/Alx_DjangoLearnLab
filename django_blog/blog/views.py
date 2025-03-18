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
    template_name = 'blog/list.html'
    context_object_name = 'posts'

# View details of a single post
class DetailViewPost(DetailView):
    model = Post
    template_name = 'blog/viewing.html'

# Create a new post
class CreateViewPost(CreateView, LoginRequiredMixin):
    model = Post
    form_class = FormPost 
    template_name = 'blog/create.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user # Assigns logged in user as author
        return super().form_valid(form)
    
# Update a post (only authors can update)
class UpdateViewPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = FormPost
    template_name = 'blog/edit.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author # Only author can edit

# Delete a post (only authors can delete a post)
class DeleteViewPost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author # Only author can delete 

def CommentCreateView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save() 
            return redirect('post-detail', pk=post.pk)
        else:
            form = CommentForm()
        return render(request, 'blog/view.html', {'post': post, 'comments': comments, 'form': form})
    
@login_required
def CommentUpdateView(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author:
        return redirect('post-detail', pk=comment.post.pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=comment.post.pk) 
        
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {'form': form})

@login_required
def CommentDeleteView(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author:
        return redirect('post-detail', pk=comment.post.pk)
    
    if request.method == 'POST':
        post_pk = comment.post.pk
        comment.delete()
        return redirect('post-detail', pk=post_pk)
    
    return render(request, 'blog/delete.html', {'comment': comment})

