from django.urls import path
from .views import RegisterUserView, LoginView, UserFollowingViewSet

urlpatterns = [
    path('register/', RegisterUserView, name='register'),
    path('login/', LoginView, name='login'),
    path('follow/<int:user_id>/',  UserFollowingViewSet.as_view({'post': 'create'}), name='follow-user'),
    path('unfollow/<int:user_id>/', UserFollowingViewSet.as_view({'delete': 'destroy'}), name='unfollow-user')

]

