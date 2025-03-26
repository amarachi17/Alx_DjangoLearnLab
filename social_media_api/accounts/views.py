from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser, UserFollowing
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status, viewsets


User = get_user_model()

# Create your views here.
class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes =[AllowAny]

    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)
    #     user = User.objects.get(username=request.data['username'])
    #     token, created = Token.objects.get_or_create(user=user)
    #     response.data['token'] = token.key 
    #     return response
   
class LoginView(APIView):
    permission_classes =[AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=200)
        
        return Response({"error": "Invalid credentials"}, status=400)

class UserProfileView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserFollowingViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request, user_id=None):
        following_user = get_object_or_404(User, id=user_id)
        if request.user == following_user:
            return Response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_REQUEST)
        UserFollowing.objects.get_or_create(user=request.user, following_user=following_user)
        return Response({'status': 'following'}, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, user_id=None):
        following_user = get_object_or_404(User, id=user_id)
        UserFollowing.objects.filter(user=request.user, following_user=following_user).delete()
        return Response({'status': 'unfollowed'}, status=status.HTTP_204_NO_CONTENT)

