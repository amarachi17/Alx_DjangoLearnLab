from django.urls import path
from  .views import Register, Login, Logout, profile_view
from .views import ListViewPost, DeleteViewPost, CreateViewPost, UpdateViewPost, DetailViewPost

urlpatterns = [
    path('register/', Register, name='register'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('posts/', ListViewPost, name='post-list'),
    path('posts/<int:pk>', DetailViewPost.as_view, name='post-detail'),
    path('posts/new/', CreateViewPost.as_view, name='post-create'),
    path('posts/<int:pk>/edit/', UpdateViewPost.as_view, name='post-update'),
    path('posts/<int:pk>/delete/', DetailViewPost.as_view, name='post-delete'),
]
