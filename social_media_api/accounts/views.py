from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser


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

