from django.urls import path
from  .views import Register, Login, Logout, profile_view
from .views import ListViewPost, DeleteViewPost, CreateViewPost, UpdateViewPost, DetailViewPost

urlpatterns = [
    path('register/', Register, name='register'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('post/', ListViewPost, name='post-list'),
    path('post/<int:pk>', DetailViewPost.as_view, name='post-detail'),
    path('post/new/', CreateViewPost.as_view, name='post-create'),
    path('post/<int:pk>/update/', UpdateViewPost.as_view, name='post-update'),
    path('post/<int:pk>/delete/', DetailViewPost.as_view, name='post-delete'),
]
