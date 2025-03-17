from django.urls import path
from  .views import Register, Login, Logout, profile_view

urlpatterns = [
    path('register/', Register, name='register'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('profile/', profile_view, name='profile'),
]
