from django.urls import path
from .views import RegisterUserView, LoginView

urlpatterns = [
    path('register/', RegisterUserView, name='register'),
    path('login/', LoginView, name='login'),
    path('profile/', )
]
