from django.urls import path
from  .views import Register, Login, Logout, profile_view, search_posts
from .views import ListViewPost, DeleteViewPost, CreateViewPost, UpdateViewPost, DetailViewPost
from .views import CommentCreateView, CommentDeleteView, CommentUpdateView
from .views import PostByTagListView, search_posts
from .models import Post

urlpatterns = [
    path('register/', Register, name='register'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('posts/', ListViewPost, name='post-list'),
    path('posts/<int:pk>', DetailViewPost.as_view, name='post-detail'),
    path('posts/new/', CreateViewPost.as_view, name='post-create'),
    path('posts/<int:pk>/update/', UpdateViewPost.as_view, name='post-update'),
    path('posts/<int:pk>/delete/', DetailViewPost.as_view, name='post-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView, name='post-detail'),
    path('comment/<int:pk>/update/', CommentUpdateView, name='comment-edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView, name='comment-delete'),
    path('search/', search_posts, name='search-posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='tagged-posts'),
]
